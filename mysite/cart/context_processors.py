from .models import CartItem, Cart

def cart_item_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        items = cart.items.all()
        item_count = sum(item.quantity for item in items)
    else:
        item_count = 0
    return {'cart_item_count': item_count}