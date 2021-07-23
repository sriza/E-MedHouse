
from django.urls import path
from . import views

urlpatterns = [
      path('checkout/<int:id>/',views.checkout),
      path('payment/<int:id>/',views.payment),
      path('paymentMade/<int:id>/',views.paymentMade),
      path('cancel/<int:id>/',views.cancelOrder),
      path('update/completed/<int:id>', views.statusCompleted),
      path('update/processing/<int:id>', views.statusProcessing),
]
