from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('track.urls')),  # 👈 This line includes your app's URLs
]
