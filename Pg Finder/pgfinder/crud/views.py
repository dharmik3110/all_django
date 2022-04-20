from django.forms import PasswordInput
from django.shortcuts import render
from django.views.generic.edit import  CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView

from .models import Pg

# Create your views here.

class Createpg(CreateView):
    model = Pg
    fields = ['pg_name','pg_address','pg_rooms','phone_number']
    template_name = 'crud/create_pg.html'
    success_url = '/crud/view/'

class Viewpg(ListView):
    model = Pg
    pgowners = model.objects.all()
    context_object_name = 'pgowners'
    template_name = 'crud/view_pg.html'  
    success_url = '/crud/view'

class Detailofpg(DetailView):
    model =  Pg
    context_object_name = 'pgowner'
    template_name = 'crud/detail_pg.html'

class Deletepg(DeleteView):
    model = Pg
    template_name = "crud/delete.html"
    success_url = '/crud/view'


class Updatepg(UpdateView):
    model = Pg
    fields = ['pg_name','pg_address','pg_rooms','phone_number']
    template_name = 'crud/update_pg.html'
    success_url = '/crud/view/'




