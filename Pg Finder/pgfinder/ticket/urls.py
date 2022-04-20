from django import views
from django.urls import path
from .views import CreateTicket, DeleteTicket , UpdateTicket,detailticket
from ticket import views



urlpatterns = [
   
   
    path( 'add/',CreateTicket.as_view()),
    path('view/', views.index),
    path('<pk>/delete/',DeleteTicket.as_view()),
    path('<pk>/update/',UpdateTicket.as_view()),
    path('<pk>/detail/',detailticket.as_view()),
    



    


]