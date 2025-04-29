from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from accounts.models import Cart, CartItems
from .models import Category, SizeVariant, ColorVariant
from django.shortcuts import get_object_or_404,  render
from products.models import Product
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, ProductImageForm
from .models import Product, ProductImage
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import uuid
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# View to create a product
# @login_required
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)
        
        if form.is_valid() and image_form.is_valid():
            product = form.save(commit=False)
            product.save()
            form.save_m2m()  # Save many-to-many relationships

            image = image_form.save(commit=False)
            image.product = product
            image.save()

            return redirect('product_list')  # Redirect to product list page

    else:
        form = ProductForm()
        image_form = ProductImageForm()

    return render(request, 'product_form.html', {'form': form, 'image_form': image_form})

# View to update a product
# @login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect after update

    else:
        form = ProductForm(instance=product)

    return render(request, 'product_form.html', {'form': form, 'product': product})

# View to delete a product
# @login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    return render(request, 'confirm_delete.html', {'product': product})

# View to list all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def add_to_cart(request, uid):
    try:
        # Convert string UID to UUID
        product_uid = uuid.UUID(uid)
    except ValueError:
        return JsonResponse({'error': 'Invalid product ID'}, status=400)

    # Fetch the product using the valid UUID
    product = get_object_or_404(Product, uid=product_uid)

    # Ensure user is authenticated
    # if request.user.is_anonymous:
    #     return JsonResponse({'error': 'You must be logged in to add items to the cart.'}, status=403)

    # Fetch or create cart for the logged-in user
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Add product to the cart
    cart.products.add(product)

    return JsonResponse({'message': 'Product added to cart successfully!'})

# def get_product(request ,product_id, product_slug):
#     try:
#         product = Product.objects.get( id=product_id, slug=product_slug)
#         context = {'product' : product}
#         if request.GET.get('size'):
#             size=request.GET.get('size')
#             price=product.get_product_price_by_size(size)
#             context['selected_size']=size
#             context['updated_price']=price
            
#         return render(request  , 'product/product.html' , context = context)

#     except Exception as e:
#         print(e)
        

def get_product(request, slug):
    try:
        # ✅ Ensure the product exists, otherwise return 404
        product = get_object_or_404(Product, slug=slug)
        context = {'product': product}

        # ✅ Get size from request and calculate price
        size = request.GET.get('size')
        if size:
            context['selected_size'] = size
            context['updated_price'] = product.get_product_price_by_size(size)  # ✅ Call the function
        
        # Get similar products from the same category, excluding the current product
        similar_products = []
        if product.category:
            similar_products = Product.objects.filter(
                category=product.category
            ).exclude(
                slug=slug
            ).order_by('?')[:4]  # Get up to 4 random products from the same category
            
        context['similar_products'] = similar_products

        return render(request, 'product/product.html', context)  # ✅ Always return a valid response

    except Product.DoesNotExist:
        return HttpResponseNotFound("<h1>Product not found</h1>")  # ✅ Handle missing product

    except Exception as e:
        print(f"Error in get_product: {e}")  # ✅ Print error in terminal
        return HttpResponse("<h1>Something went wrong. Please try again later.</h1>", status=500)
        
        
def buy_now(request,id):
    product =get_object_or_404(Product,id=id)
   
    return render(request , 'product/buy_now.html' , {'peoduct': product})

def home(request):
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'product/category.html', {'categories': categories})

def category_filter(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug) 
    # Fetch products related to this category
    products_list = Product.objects.filter(category=category)
    
    # Handle sorting
    sort = request.GET.get('sort', '')
    if sort == 'price_asc':
        products_list = products_list.order_by('price')
    elif sort == 'price_desc':
        products_list = products_list.order_by('-price')
    elif sort == 'name_asc':
        products_list = products_list.order_by('product_name')
    elif sort == 'name_desc':
        products_list = products_list.order_by('-product_name')
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products_list, 12)  # Show 12 products per page
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    # Pass data to the template
    return render(request, 'product/category.html', {
        'category': category,
        'products': products,
        'sort': sort,  # Pass the current sort parameter to the template
    })
    
# def add_to_cart(request,uid):
#     variant=request.GET.get('variant')
#     product=Product.objects.get(uid=uid)
#     user=request.user
#     cart, _=Cart.objects.get_or_create(user=user,is_paid=False)
    
#     cart_items=CartItems.objects.create(cart=cart,product=product,)
    
#     if variant:
#         variant=request.GET.get('varaint')
#         size_variant=SizeVariant.objects.get(size_name=variant)
#         cart_items,size_variant=size_variant
#         cart_items.save()
        
        
    
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def cart_view(request):
    # Example: Assuming you store the cart items in the session or model
    cart_items = request.session.get('cart_items', [])
    return render(request, 'accounts/cart_item.html', {'cart_items': cart_items})

def add_product(request):
    """
    View for adding a new product with images
    """
    from .models import Category, ColorVariant, SizeVariant, Product, ProductImage
    from .forms import ProductForm, ProductImageForm
    from django.shortcuts import render, redirect
    
    # Get all categories, colors and sizes for the form
    categories = Category.objects.all()
    colors = ColorVariant.objects.all()
    sizes = SizeVariant.objects.all()
    
    if request.method == 'POST':
        # Debug: Print the POST data
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        
        # Create a mutable copy of the POST data
        post_data = request.POST.copy()
        
        # Handle the color_variant and size_variant fields
        # If they're not selected, remove them from the data to avoid validation errors
        if 'color_variant[]' not in post_data:
            post_data['color_variant'] = []
        else:
            post_data.setlist('color_variant', post_data.getlist('color_variant[]'))
            post_data.pop('color_variant[]')
            
        if 'size_variant[]' not in post_data:
            post_data['size_variant'] = []
        else:
            post_data.setlist('size_variant', post_data.getlist('size_variant[]'))
            post_data.pop('size_variant[]')
        
        form = ProductForm(post_data)
        
        if form.is_valid():
            # Save the product without committing to get the product instance
            product = form.save()
            
            # Handle main image
            if request.FILES.get('main_image'):
                ProductImage.objects.create(
                    product=product,
                    image=request.FILES['main_image']
                )
            
            # Handle additional images
            if request.FILES.getlist('additional_images[]'):
                for img in request.FILES.getlist('additional_images[]'):
                    ProductImage.objects.create(
                        product=product,
                        image=img
                    )
            
            messages.success(request, f'Product "{product.product_name}" has been added successfully.')
            return redirect('get_product', slug=product.slug)
        else:
            # Debug: Print form errors
            print("Form errors:", form.errors)
            messages.error(request, f'There was an error with your submission. Please check the form. Errors: {form.errors}')
    
    # Pass the context to the template
    context = {
        'categories': categories,
        'colors': colors,
        'sizes': sizes,
    }
    
    return render(request, 'products/add_product.html', context)

# API endpoints for color and size variants
@csrf_exempt
def add_color(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)
    
    try:
        print("Received add_color request")
        # Parse JSON data
        try:
            data = json.loads(request.body)
            color_name = data.get('color_name', '')
            price = int(data.get('price', 0))
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
        
        print(f"Color data: name={color_name}, price={price}")
            
        # Validate data
        if not color_name:
            return JsonResponse({'status': 'error', 'message': 'Color name is required'}, status=400)
        
        # Create the color
        color = ColorVariant()
        color.color_name = color_name
        color.price = price
        color.save()
        
        # Return success response
        return JsonResponse({
            'status': 'success',
            'message': 'Color added successfully',
            'color': {
                'uid': str(color.uid),
                'color_name': color.color_name,
                'price': color.price
            }
        })
    except Exception as e:
        print(f"Error in add_color: {str(e)}")
        import traceback
        traceback.print_exc()
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
def add_size(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)
    
    try:
        print("Received add_size request")
        # Parse JSON data
        try:
            data = json.loads(request.body)
            size_name = data.get('size_name', '')
            price = int(data.get('price', 0))
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
        
        print(f"Size data: name={size_name}, price={price}")
            
        # Validate data
        if not size_name:
            return JsonResponse({'status': 'error', 'message': 'Size name is required'}, status=400)
        
        # Create the size
        size = SizeVariant()
        size.size_name = size_name
        size.price = price
        size.save()
        
        # Return success response
        return JsonResponse({
            'status': 'success',
            'message': 'Size added successfully',
            'size': {
                'uid': str(size.uid),
                'size_name': size.size_name,
                'price': size.price
            }
        })
    except Exception as e:
        print(f"Error in add_size: {str(e)}")
        import traceback
        traceback.print_exc()
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# API endpoint for category creation
@csrf_exempt
def add_category(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)
    
    try:
        print("Received add_category request")
        # Parse JSON data
        try:
            data = json.loads(request.body)
            category_name = data.get('category_name', '')
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
        
        print(f"Category data: name={category_name}")
            
        # Validate data
        if not category_name:
            return JsonResponse({'status': 'error', 'message': 'Category name is required'}, status=400)
        
        # Create the category with a slugified name
        from django.utils.text import slugify
        
        # Start with basic slug
        base_slug = slugify(category_name)
        slug = base_slug
        counter = 1
        
        # Check if slug exists and generate a unique one if needed
        while Category.objects.filter(slug=slug).exists():
            # If slug exists, append a number to make it unique
            slug = f"{base_slug}-{counter}"
            counter += 1
        
        # Create the category with the unique slug
        category = Category()
        category.category_name = category_name
        category.slug = slug  # Set the unique slug explicitly
        category.save()
        
        # Return success response with category_id field
        return JsonResponse({
            'status': 'success',
            'message': 'Category added successfully',
            'category_id': str(category.uid),  # Use the UID as the ID for the form
            'category': {
                'uid': str(category.uid),
                'category_name': category.category_name,
                'slug': category.slug  # Include the slug in the response
            }
        })
    except Exception as e:
        print(f"Error in add_category: {str(e)}")
        import traceback
        traceback.print_exc()
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

