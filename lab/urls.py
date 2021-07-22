
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.labLogin, name="login"),
    path('signin/', views.signin, name="signin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('appointment/', views.appointment, name="appointment"),
    path('address/', views.address, name="address"),
    path('profile-details/', views.profileDetails, name="profileDetails"),
    path('service-details/', views.serviceDetails, name="serviceDetails"),
    path('forget-password/', views.forgetPassword, name="forgetPassword"),
    path('logout/', views.labLogout, name="logout"),

]
