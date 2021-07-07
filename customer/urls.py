
from django.urls import path
from . import views
<<<<<<< Updated upstream

urlpatterns = [
    path('login/', views.customerLogin),
    path('signin/', views.signin),
    path('dashboard/', views.dashboard),
    path('order/', views.order),
    path('profile-details/', views.profileDetails),
    path('forget-password/', views.forgetPassword),
    path('logout/', views.customerLogout),
]
=======

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('login/', views.login),
    path('order/',views.order),
    path('profile-details/',views.profileDetails),
    path('address/',views.address),
    path('sigin/',views.signin),
    path('forget-password/',views.forgetPassword),
]

>>>>>>> Stashed changes
