
from django.urls import path
from . import views

urlpatterns = [
    path('add/medicine/', views.createMedicine), 
    path('add/device/', views.createDevice), 
    path('add/hygenic_product/', views.createHygenicProduct),
    path('update/medicine/<int:id>', views.updateMedicine), 
    path('update/device/<int:id>', views.updateDevice), 
    path('update/hygenic_product/<int:id>', views.updateHygenicProduct),
    path('list/', views.listProduct), 
    path('detail/<int:id>', views.detailProduct), 
    path('shop/', views.shopProduct), 
    path('shop/detail/<int:id>', views.shopProductDetail), 
    path('shop/detail/<int:id>/', views.shopProductDetail), 
    path('delete/<int:id>',views.deleteProduct),
]
