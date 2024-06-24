"""
URL configuration for power_plants project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

import django.contrib.auth.views 

import app_plants_info.views 
from app_plants_info.views import *

urlpatterns = [
    path("", app_plants_info.views.home, name='home'),
    path("solar_plants/", solar_plants, name='solarplants'),
    path("hydro_plants/", hydro_plants, name='hydroplants'),
    path("wind_plants/", wind_plants, name='windplants'),
    path("gas_plants/", gas_plants, name='gasplants'),
    path("coal_plants/", coal_plants, name='coalplants'),
    path("oil_plants/", oil_plants, name='oilplants'),
    
    
    path("admin/", admin.site.urls),
]

