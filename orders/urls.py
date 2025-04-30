from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('order-status/', views.order_status, name='order_status'),
    path('add-to-cart/<int:flower_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('customize/<int:order_id>/', views.customize_order, name='customize_order'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/<int:order_id>/', views.checkout, name='checkout_with_order'),
    path('payment/', views.payment, name='payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('order_confirm/', views.order_confirm, name='order_confirm'),
]
