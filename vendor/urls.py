
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.vendorLogin, name="login"),
    path('signin/', views.signin, name="signin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('order/', views.order, name="order"),
    path('profile-details/', views.profileDetails, name="profile"),
    path('forget-password/', views.forgetPassword, name="forget-password"),
    path('logout/', views.vendorLogout, name="logout"),
    path('vendorupdate/<int:id>/', views.updateVendor, name="updateVendor")
]

