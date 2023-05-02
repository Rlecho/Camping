"""Campingbenin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from Campingbenin.camping.views import event_list_view
from camping import views
from django.contrib import admin
from django.urls import path
from camping.views import event_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('reservation/', views.reservation, name='reservation'),
    path('event_create/', views.event_create, name='event_create'),
    path('event_details/', views.event_details, name='event_details'),
     path('events/', event_list_view, name='event_list'),
]
