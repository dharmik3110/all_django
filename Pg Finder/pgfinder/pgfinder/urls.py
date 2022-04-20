"""pgfinder URL Configuration

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
from turtle import home
from homepage import views
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('owner/',include('owner.urls')),
    path('orm/',include('orm.urls')),
    path('newapp/',include('newapp.urls')),
    path('ticket/',include('ticket.urls')),
    path('pg/',include('pg.urls')),
    path('core/',include('core.urls')),
    path('form/',include('form.urls')),
    path('userapp/',include('userapp.urls')),
    path('crud/',include('crud.urls')),



   

   




    
]
