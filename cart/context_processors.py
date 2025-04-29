from .models import Cart

def cart_processor(request):
    """
    Context processor that provides cart data to all templates.
    """
    cart_id = request.session.get('cart_id')
    cart = None
    cart_item_count = 0
    
    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
            if cart.items.exists():
                cart_item_count = cart.items.count()
        except Cart.DoesNotExist:
            pass
    
    return {
        'cart': cart,
        'cart_item_count': cart_item_count
    } 