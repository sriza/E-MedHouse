
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.labLogin, name="login"),
    path('signin/', views.signin, name="signin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('appointment/', views.appointment, name="appointment"),
    path('profile-details/', views.profileDetails, name="profileDetails"),
    path('forget-password/', views.forgetPassword, name="forgetPassword"),
    path('logout/', views.labLogout, name="logout"),
    path('labupdate/<int:id>/', views.updateLab, name="updateLab"),    
]
