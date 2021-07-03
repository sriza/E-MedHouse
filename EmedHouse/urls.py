
from medicalapp import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('',include('medicalapp.urls')),
    path('',include('customer.urls')),
    path('admin/', admin.site.urls),
    
]
