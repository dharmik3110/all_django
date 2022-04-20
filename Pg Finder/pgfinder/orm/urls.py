from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from orm import views

urlpatterns = [
   
   
    path('userData/',views.userData),




]