
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createProduct), 
    path('list/', views.listProduct), 
    path('detail/<int:id>', views.detailProduct), 
]
