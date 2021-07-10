
from medicalapp import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',include('medicalapp.urls')),
    path('vendor/',include('vendor.urls')),
    path('customer/',include('customer.urls')),
    path('order/',include('order.urls')),  
    path('cart/',include('cart.urls')),  
    path('product/',include('product.urls')),  
    path('doctor/',include('doctor.urls')),  
    path('admin/', admin.site.urls),
    # path('chatbot/',include('chatbot.urls')),multiple pharmacies always present to help your need
    path('lab/',include('lab.urls')),
    path('service/',include('service.urls')),
    
]
# urlpatterns += static(settings.MEDIA_)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)