
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('doctor/', views.doctor),
    path('shop/', views.shop),
    path('login/', views.login),
    path('signin/', views.signin),
]
