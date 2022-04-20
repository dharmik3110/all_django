from lib2to3.pgen2.token import COMMENT
from pyexpat import model
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView,LogoutView
from .forms import UserSignupForm

# Create your views here.

class Login(LoginView):
    template_name = "core/login.html"
    success_url = '/admin'

class logout(LogoutView):
   pass



def signup(request):
    if request.POST:
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserSignupForm()
    return render(request,"core/login.html",{"form": form})


