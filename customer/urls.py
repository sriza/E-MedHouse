
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('signin/', views.signin),
    path('dashboard/', views.dashboard),
    path('order/', views.order),
    path('address/', views.address),
    path('profile-details/', views.profileDetails),
    path('forget-password/', views.forgetPassword),
]
