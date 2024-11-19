"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import hello_world, hello_world_api, register, login  # Import both views
from .api.vpet_views import create_vpet, get_vpets, get_vpet, update_vpet, delete_vpet  # Import the new views


urlpatterns = [
    path('api/auth/register/', register, name='register'),
    path('api/auth/login/', login, name='login'),
    path('admin/', admin.site.urls),
    path('hello/', hello_world),  # Existing view for "Hello World" (HTML response)
    path('api/hello/', hello_world_api),  # New API endpoint for "Hello World" (JSON response)
    path('api/vpets/', get_vpets, name='get_vpets'),  # GET all Vpets
    path('api/vpets/<int:vpet_id>/', get_vpet, name='get_vpet'),  # GET a specific Vpet
    path('api/vpets/create/', create_vpet, name='create_vpet'),  # Create a new Vpet
    path('api/vpets/update/<int:vpet_id>/', update_vpet, name='update_vpet'),  # Update a specific Vpet
    path('api/vpets/delete/<int:vpet_id>/', delete_vpet, name='delete_vpet'),  # Delete a specific Vpet
    
]