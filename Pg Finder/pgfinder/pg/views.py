from django.forms import PasswordInput
from django.shortcuts import render
from django.views.generic.edit import  CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView

from .models import NewOwner
    

# Create your views here.

class CreateOwner(CreateView):
    model = NewOwner
    fields = ['owner_name','owner_email','owner_address','owner_phonenumber']
    template_name = 'pg/create_owner.html'
    success_url = '/pg/view/'

class ViewOwner(ListView):
    model = NewOwner
    newowners = model.objects.all()
    context_object_name = 'newowners'
    template_name = 'pg/view_owner.html'  
    success_url = '/pg/view'

class DetailOwner(DetailView):
    model =  NewOwner
    context_object_name = 'newowner'
    template_name = 'pg/detail_owner.html'

class DeleteOwner(DeleteView):
    model = NewOwner
    template_name = "pg/delete.html"
    success_url = '/pg/view'


class UpdateOwner(UpdateView):
    model = NewOwner
    fields = ['owner_name','owner_email','owner_address','owner_phonenumber']
    template_name = 'pg/update_owner.html'
    success_url = '/pg/view/'




