from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from orders.models import  Order,  OrderItem, CartItem 
from flowers.models import Flower 
from .forms import CustomizationForm
from django.contrib import messages


@login_required
def order_status(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'orders/order_status.html', {'orders': orders})

@login_required
def add_to_cart(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, flower=flower)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        for item in items:
            qty_field = f'quantity_{item.id}'
            new_qty = int(request.POST.get(qty_field, item.quantity))
            if new_qty != item.quantity:
                item.quantity = new_qty
                item.save()
        return redirect('cart')  
    total = sum(item.total_price() for item in items)
    return render(request, 'orders/cart.html', {'items': items, 'total': total})

@login_required
def checkout(request, order_id=None):
    if order_id:
        order = get_object_or_404(Order, id=order_id, user=request.user)
    else:
        items = CartItem.objects.filter(user=request.user)
        if not items:
            return redirect('cart')
        if request.method == 'POST':
            address = request.POST.get('address')
            order = Order.objects.create(user=request.user, delivery_address=address)
            for item in items:
                OrderItem.objects.create(order=order, flower=item.flower, quantity=item.quantity)
            items.delete()
            return redirect('customize_order', order_id=order.id)
        return render(request, 'orders/checkout.html')
    return render(request, 'orders/checkout.html', {'order': order})

 
@login_required
def customize_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        form = CustomizationForm(request.POST)
        if form.is_valid():
            customization = form.save(commit=False)
            customization.order = order  
            customization.save()
            return redirect('payment')
    else:
        form = CustomizationForm()

    return render(request, 'orders/customize_order.html', {'form': form, 'order': order})


@login_required
def payment(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')

        if payment_method == 'cod':
            return redirect('order_confirm')  

        elif payment_method == 'card':
            card_number = request.POST.get('card_number')
            expiry = request.POST.get('expiry')
            cvv = request.POST.get('cvv')

            if card_number and expiry and cvv:
                return redirect('payment_success')   
            else:
                return redirect('payment')  

    return render(request, 'orders/payment.html')  


@login_required
def payment_success(request):
    return render(request, 'orders/payment_success.html')

@login_required
def order_confirm(request):
    return render(request, 'orders/order_confirm.html')
