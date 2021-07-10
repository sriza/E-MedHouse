
from django.urls import path
from . import views

urlpatterns = [
  path('list/',views.cart),
  path('add/<int:id>', views.addToCart),
  path('remove/<int:id>', views.removeFromCart),
]
