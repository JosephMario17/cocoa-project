from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('service/', views.serviceDetails, name='service-details'),
    path('contact/', views.contact, name='contact'),
    
    path('custom-cocoa/', views.custom, name='custom'),
    path('bulk-supply/', views.bulk, name='bulk'),
    path('processing/', views.processing, name='processing'),
    path('sourcing/', views.sourcing, name='sourcing'),
    path('training/', views.training, name='training'),

    path('thanks/', views.thankYou, name='thank-you'),
]