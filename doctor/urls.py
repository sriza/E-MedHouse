
from django.http.response import HttpResponseNotModified
from customer.views import doctor
from django.http import request
from django.urls import path
from . import views

urlpatterns = [
  path('login/',views.doctorLogin),
  path('signin/',views.signin),
  path('dashboard/',views.dashboard),
  path('order/',views.order),
  path('profile-details/',views.profileDetails),
]
