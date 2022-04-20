
from django import views
from django.urls import path


from .views import Createpg, Deletepg, Detailofpg, Updatepg,Viewpg




urlpatterns = [
   
   
    path( 'createpg/',Createpg.as_view(), name = 'create_pg'),
    path('view/', Viewpg.as_view(), name = 'view_pg'),
    path('<int:pk>/delete/',Deletepg.as_view(),name = 'delete_pg'),
    path('<int:pk>/update/',Updatepg.as_view(),name = 'update_pg'),
    path('<int:pk>/view/',Detailofpg.as_view(),name = 'detail_pg'),
    
    


    


]