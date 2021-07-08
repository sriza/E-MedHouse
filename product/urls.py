
from django.urls import path
from . import views

urlpatterns = [
    path('add/medicine/', views.createMedicine), 
    path('add/device/', views.createDevice), 
    path('add/hygenic_product/', views.createHygenicProduct), 
    path('list/', views.listProduct), 
    path('detail/<int:id>', views.detailProduct), 
    path('shop/', views.shopProduct), 
    path('shop/detail/<int:id>', views.shopProductDetail), 

]
