from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.models import Cart
def order_create(request):
    cart = Cart.objects.get(user=request.user)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart.items.all():
                OrderItem.objects.create(order=order, product=item.product, price=item.product.price, quantity=item.quantity)
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})