# myapp/urls.py
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('contact-us/', views.Contact_Us, name='contact_us'),
    path('property-owners/', views.Property_Owners, name='property_owners'),
    path('request-electronic-contract/', views.Request_Electronic_Contract, name='request_electronic_contract'),
    path('about-us/', views.about_us, name='about_us'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)