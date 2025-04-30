from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_flowers, name='search_flowers'),
    path('bestsellers/', views.bestsellers, name='bestsellers'),
    path('seasonal/', views.seasonal, name='seasonal'),
    path('new/', views.new_flowers, name='new_flowers'),
    path('<int:id>/', views.flower_detail, name='flower_detail'),
    path('budget/', views.budget_view, name='budget'),
]
