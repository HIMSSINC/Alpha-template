"""LeadGenAlpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from leadgen import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('acousticceilings/', views.multistepformsubmissionacousticceilings.as_view(), name='acousticceilings'),
    path('bathroom/', views.multistepformsubmissionbathroom.as_view(), name='bathroom'),
    path('flooring/', views.multistepformsubmissionflooring.as_view(), name='flooring'),
    path('homebuilder/', views.multistepformsubmissionhomebuilder.as_view(), name='homebuilder'),
    path('landscaping/', views.multistepformsubmissionlandscaping.as_view(), name='landscaping'),
    path('roofing/', views.multistepformsubmissionroofing.as_view(), name='roofing'),
    path('stonetile/', views.multistepformsubmissionstonetile.as_view(), name='stonetile'),
    path('swimmingpool/', views.multistepformsubmissionswimmingpool.as_view(), name='swimmingpool'),

]
