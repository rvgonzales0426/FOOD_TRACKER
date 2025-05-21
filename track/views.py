from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem, DonationCenter
from .forms import FoodItemForm, DonationCenterSearchForm, CustomUserCreationForm
from django.db.models import Count, Sum, Q
from django.http import HttpResponseNotAllowed
import math
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='landing')
def home(request):
    items = FoodItem.objects.all().order_by('-created_at')
    total_quantity = FoodItem.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
    surplus_quantity = FoodItem.objects.filter(is_surplus=True).aggregate(Sum('quantity'))['quantity__sum'] or 0
    non_surplus_quantity = FoodItem.objects.filter(is_surplus=False).aggregate(Sum('quantity'))['quantity__sum'] or 0
    surplus_percentage = (surplus_quantity / total_quantity * 100) if total_quantity else 0
    
    return render(request, 'track/home.html', {
        'items': items,
        'surplus_quantity': surplus_quantity,
        'non_surplus_quantity': non_surplus_quantity,
        'surplus_percentage': surplus_percentage,
    })

def landing(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'track/landing.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'track/login.html')

def logout_view(request):
    logout(request)
    return redirect('landing')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'track/register.html', {'form': form})

@login_required(login_url='landing')
def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoodItemForm()
    return render(request, 'track/add_food.html', {'form': form})

@login_required(login_url='landing')
def report(request):
    total_items = FoodItem.objects.count()
    total_quantity = FoodItem.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
    category_count = FoodItem.objects.values('category').annotate(count=Count('id'))

    surplus_quantity = FoodItem.objects.filter(is_surplus=True).aggregate(Sum('quantity'))['quantity__sum'] or 0
    non_surplus_quantity = FoodItem.objects.filter(is_surplus=False).aggregate(Sum('quantity'))['quantity__sum'] or 0
    surplus_percentage = (surplus_quantity / total_quantity * 100) if total_quantity else 0

    return render(request, 'track/report.html', {
        'total_items': total_items,
        'total_quantity': total_quantity,
        'category_count': category_count,
        'surplus_quantity': surplus_quantity,
        'non_surplus_quantity': non_surplus_quantity,
        'surplus_percentage': surplus_percentage,
    })

@login_required(login_url='landing')
def pickup_confirm(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    if request.method == 'POST':
        # Confirm pickup, delete the food item
        food_item.delete()
        return redirect('home')
    return render(request, 'track/pickup_confirm.html', {'food_item': food_item})

@login_required(login_url='landing')
def pickup_food(request, food_id):
    # Redirect to pickup_confirm page
    return redirect('pickup_confirm', food_id=food_id)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

@login_required(login_url='landing')
def search_donation_centers(request):
    results = None
    if request.method == 'POST':
        form = DonationCenterSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('query', '').strip()
            if query:
                results = DonationCenter.objects.filter(
                    Q(name__icontains=query) | Q(location__icontains=query)
                )
            else:
                results = []
    else:
        form = DonationCenterSearchForm()
    return render(request, 'track/search_donation_centers.html', {'form': form, 'results': results})
