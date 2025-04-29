from django.shortcuts import render
from products.models import Product
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def search_view(request):
    query = request.GET.get('search_query')  # Get the search input
    products_list = []
    sort = ''
    
    if query:
        products_list = Product.objects.filter(product_name__icontains=query)
        
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
        
        print("Products Found:", products_list)
        
        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(products_list, 12)  # Show 12 products per page
        
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    else:
        products = []

    return render(request, 'home/search-view.html', {
        'query': query, 
        'products': products,
        'sort': sort,  # Pass the current sort parameter to the template
    })


def index(request):
    # Get all products for main shop section
    all_products = Product.objects.all().order_by('-created_at')
    
    # Get new arrivals (products added in the last 30 days)
    thirty_days_ago = timezone.now() - timedelta(days=30)
    new_arrivals = Product.objects.filter(created_at__gte=thirty_days_ago).order_by('-created_at')[:8]
    
    context = {
        'products': all_products,
        'new_arrivals': new_arrivals,
    }
    
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about1.html')



