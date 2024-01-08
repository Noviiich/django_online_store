from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from shop.models import Product

def cart_detail(request):
    try:
        cart = Cart.objects.get(user=request.user)
        items = cart.items.all()
        total = sum(item.product.price * item.quantity for item in items)
        item_count = sum(item.quantity for item in items)
        for item in items:
            item.total_price = item.product.price * item.quantity
    except Cart.DoesNotExist:
        cart = None
    context = {
        'total': total,
        'items': items,
        'item_count': item_count,
    }
    return render(request, 'cart/test.html', context)
@login_required
def cart_add(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart:cart_detail')
@login_required
def cart_remove(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(CartItem, product__id=product_id, cart=cart)
    product.delete()
    return redirect('cart:cart_detail')


def cart_update(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(CartItem, product__id=product_id, cart=cart)
    action = request.POST.get('action')

    if action == 'add':
        product.quantity += 1
    elif action == 'subtract' and product.quantity > 1:
        product.quantity -= 1

    product.save()
    return redirect('cart:cart_detail')
