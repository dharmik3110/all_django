#from dataclasses import fields

#from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.edit import  CreateView,DeleteView,UpdateView
from django.views.generic import DetailView
from ticket.models import Ticket
    

# Create your views here.

class CreateTicket(CreateView):
    model = Ticket
    fields = ['ticket_title','ticket_description']
    template_name = 'ticket/create_ticket.html'

# del ma success url , model

class DeleteTicket(DeleteView):
    model = Ticket
    success_url = '/ticket/view/'

def index(request):
    return render(request,'ticket/index.html')

class UpdateTicket(UpdateView):
    model = Ticket
    fields = ['ticket_title','ticket_description']
    template_name = 'ticket/Update_ticket.html'
    success_url = '/ticket/view/'

class detailticket(DetailView):
    model = Ticket
    fields = ['ticket_title','ticket_description']
    template_name = 'ticket/task_detail.html'
    success_url = '/ticket/view/'


