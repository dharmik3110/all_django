from unicodedata import name
from django import views
from django.urls import path
from .views import CreateAddress
from form import views


urlpatterns = [
   
   
    path('createaddress/',CreateAddress.as_view(), name = 'create'),
    

    


]