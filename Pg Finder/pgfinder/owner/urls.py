from django.contrib import admin
from django.urls import path
from owner import views

urlpatterns = [
   
   
    path('ContactUs/',views.ContactUs),
    path('AboutUs/',views.AboutUs),
    path('index/',views.index),
   




]