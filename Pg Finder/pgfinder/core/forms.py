from dataclasses import field, fields
import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
        