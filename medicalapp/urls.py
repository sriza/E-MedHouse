
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('doctor/', views.doctor),
    path('shop/', views.shop),
    path('login/', views.login),
    path('signin/', views.signin),
    path('dashboard/', views.dashboard),
    path('order/', views.order),
    path('address/', views.address),
    path('profile-details/', views.profileDetails),
    path('forget-password/', views.forgetPassword),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('confirmation/', views.confirmation),
    path('contact/', views.contact),
    path('shop-sidebar/', views.shopslider),
]
