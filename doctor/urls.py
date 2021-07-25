
from django.http.response import HttpResponseNotModified
from customer.views import doctor
from django.http import request
from django.urls import path
from . import views

urlpatterns = [
  path('login/',views.doctorLogin),
  path('signin/',views.signin),
  path('dashboard/',views.dashboard),
  path('appointmentList/',views.appointmentList),
  path('profile-details/',views.profileDetails),
  path('appointment/<int:id>/',views.appointment),
  path('appointment/update/<int:id>/',views.updateAppointment),
  path('status/completed/<int:id>/',views.statusCompleted),
  path('payment/<int:id>/',views.payment),
  path('paymentMade/<int:id>/',views.paymentMade),
  path('appointment/cancel/<int:id>/',views.cancelAppointment),
]
