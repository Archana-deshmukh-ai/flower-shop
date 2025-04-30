from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('contact_form/', views.contact_form, name='contact_form'),
    
]
