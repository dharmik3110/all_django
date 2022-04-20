from django import views
from django.urls import path
from .views import CreateOwner,ViewOwner,DetailOwner,DeleteOwner,UpdateOwner
from core import views



urlpatterns = [
   
   
    path( 'createowner/',CreateOwner.as_view(), name = 'create_owner'),
    path('view/', ViewOwner.as_view(), name = 'view_owner'),
    path('<int:pk>/delete/',DeleteOwner.as_view(),name = 'delete_owner'),
    path('<int:pk>/update/',UpdateOwner.as_view(),name = 'update_owner'),
    path('<int:pk>/view/',DetailOwner.as_view(),name = 'detail_owner'),
    
    


    


]