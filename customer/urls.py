
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.customerLogin),
    path('signin/', views.signin),
    path('doctor/', views.doctor),
    path('dashboard/', views.dashboard),
    path('order/', views.order),
    path('doctor-appointment/', views.doctorAppointmentList),
    path('forget-password/', views.forgetPassword),
    path('logout/', views.customerLogout),
    path('vendors/', views.vendors),
    path('lab/', views.lab),
    path('lab-detail/<int:id>/', views.labDetails),
    path('appointment/', views.appointment),
]

