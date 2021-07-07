
from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.vendorLogin),
    # path('signin/', views.signin),
    # path('dashboard/', views.dashboard),
    # path('order/', views.order),
    # path('address/', views.address),
    # path('profile-details/', views.profileDetails),
    # path('product-details/', views.productDetails),
    path('login/', views.vendorLogin, name="login"),
    path('signin/', views.signin, name="signin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('order/', views.order, name="order"),
    path('address/', views.address, name ="address"),
    path('profile-details/', views.profileDetails, name="profile"),
    path('forget-password/', views.forgetPassword, name="forget-password"),
    path('logout/', views.vendorLogout, name="logout"),
]

