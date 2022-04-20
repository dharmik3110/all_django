from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [
   
   
     path('addStudent/',views.addStudent),
     path('viewStudent/',views.viewStudent),
     path('delStudent/',views.delStudent),
     path('updateStudent/',views.updateStudent),





]