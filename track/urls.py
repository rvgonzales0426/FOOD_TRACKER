from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('add/', views.add_food, name='add_food'),
    path('report/', views.report, name='report'),
    path('search-donation-centers/', views.search_donation_centers, name='search_donation_centers'),
    path('pickup/<int:food_id>/', views.pickup_food, name='pickup_food'),
    path('pickup-confirm/<int:food_id>/', views.pickup_confirm, name='pickup_confirm'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
