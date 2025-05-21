from django import forms
from .models import FoodItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'quantity', 'quantity_unit', 'category', 'is_surplus', 'donation_center']
        widgets = {
            'quantity_unit': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_surplus': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'donation_center': forms.Select(attrs={'class': 'form-select'}),
        }

class DonationCenterSearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False)

class CustomUserCreationForm(UserCreationForm):
    def clean_password2(self):
        # Override to disable password complexity validation
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("The two password fields didn't match.")
        return password2

    class Meta:
        model = User
        fields = ("username",)

