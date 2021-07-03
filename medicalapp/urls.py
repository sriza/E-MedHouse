
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('doctor/', views.doctor),
    path('shop/', views.shop),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('confirmation/', views.confirmation),
    path('contact/', views.contact),
    path('shop-sidebar/', views.shopslider),
]
