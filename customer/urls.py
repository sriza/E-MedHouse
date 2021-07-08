
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.customerLogin),
    path('signin/', views.signin),
    path('doctor/', views.doctor),
    path('dashboard/', views.dashboard),
    path('order/', views.order),
    path('profile-details/', views.profileDetails),
    path('forget-password/', views.forgetPassword),
    path('logout/', views.customerLogout),
    path('vendors/', views.vendors),
    path('vendor-detail/<int:id>/', views.vendorDetails),
]

