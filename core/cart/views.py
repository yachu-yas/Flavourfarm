from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartItem

@login_required
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user, is_active=True)
        context = {'cart': cart}
    except Cart.DoesNotExist:
        context = {'cart': None}
    return render(request, 'cart/cart.html', context)

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('view_cart')

@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    quantity = request.POST.get('quantity')
    if quantity.isdigit() and int(quantity) > 0:
        cart_item.quantity = int(quantity)
        cart_item.save()
        messages.success(request, "Cart updated.")
    else:
        messages.error(request, "Invalid quantity.")
    return redirect('view_cart')
