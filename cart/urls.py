
from django.urls import path
from . import views

urlpatterns = [
  path('cart/',views.cart)
    # path('add/', views.addToCart),
]
