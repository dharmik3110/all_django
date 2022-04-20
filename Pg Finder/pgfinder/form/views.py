from sre_constants import SUCCESS
import django
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import AddressForm
from .models import Address

# Create your views here.

class CreateAddress(CreateView):
    form_class = AddressForm
    model = Address
    template_name = 'form/address_forms.html'
    success_url = '/pg/view/'