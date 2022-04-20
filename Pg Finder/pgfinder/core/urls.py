from unicodedata import name
from django import views
from django.urls import path
from .views import Login,logout
from core import views


urlpatterns = [
   
   
    path('Login/',Login.as_view(), name = 'login'),
    path('Logout/',logout.as_view(), name = 'dharmik'),
    path("signup/",views.signup, name="signup"),


    


]