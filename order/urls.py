
from django.urls import path
from . import views

urlpatterns = [
      path('checkout/',views.checkout),
      path('quantity/', views.quantity),
      # path('add/', views.createOrder, name="login"),
]
