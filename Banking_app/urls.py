from django.contrib import admin 
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('view_cust', views.view_cust),
    path('add_customer', views.add_customer),
   # path('remove_cust',views.remove_cust),
  #  path('remove_cust/<int:cust_id',views.remove_cust),
]