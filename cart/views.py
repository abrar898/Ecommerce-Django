from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Cart, CartItem
from django.http import JsonResponse, HttpResponse
import xhtml2pdf.pisa as pisa
from io import BytesIO
import datetime
import uuid
from django.template.loader import get_template
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Cart, CartItem, Product  
# @require_POST
def cart_add(request, slug):
    print(f"Received slug: {slug}")  # Debugging line

    if not slug:
        return JsonResponse({'error': 'Invalid product slug'}, status=400)

    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    # Fix: Use slug to fetch the product
    product = get_object_or_404(Product, slug=slug)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    print(f"Added to cart: {cart_item}")  

    return redirect("cart_detail")



def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = None
    
    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
    
    # Return JSON for AJAX requests
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or 'application/json' in request.headers.get('Accept', ''):
        count = cart.items.count() if cart and cart.items.exists() else 0
        return JsonResponse({'count': count})
    
    # Return normal template for regular requests    
    if not cart or not cart.items.exists():
        cart = None
    
    return render(request, "cart/detail.html", {"cart": cart})
    


def cart_remove(request, slug):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    product = get_object_or_404(Product, slug=slug)
    cart_item = get_object_or_404(CartItem, product=product, cart=cart)
    cart_item.delete()

    return redirect("cart_detail") 
    

# New checkout function for PDF generation
def checkout(request):
    cart_id = request.session.get('cart_id')
    
    if not cart_id:
        return redirect("cart_detail")
    
    cart = get_object_or_404(Cart, id=cart_id)
    
    if not cart.items.exists():
        return redirect("cart_detail")
    
    # Generate unique receipt ID
    receipt_id = f"INV-{uuid.uuid4().hex[:8].upper()}"
    
    # Calculate total price
    total_price = sum(item.product.price * item.quantity for item in cart.items.all())
    
    # Create PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{receipt_id}.pdf"'
    
    # Create PDF content
    pdf = generate_pdf('cart/receipt_template.html', {
        'cart': cart,
        'cart_items': cart.items.all(),
        'total_price': total_price,
        'date': datetime.datetime.now(),
        'receipt_id': receipt_id
    })
    
    # Write PDF to response
    response.write(pdf)
    
    # Clear the cart after successful checkout
    # Comment this out if you want to keep the cart until payment processing is complete
    cart.items.all().delete()
    # Or alternatively mark cart as processed
    # cart.is_processed = True
    # cart.save()
    # request.session.pop('cart_id', None)  # Remove cart from session
    
    return response

def generate_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None