from django.shortcuts import get_object_or_404, render

from products.models import Product

def profiles(request):
    return render(request, 'admin/profiles.html')

def user(request):
    return render(request, 'admin/user.html')


def home(request):
    return render(request, 'admin/admin.html')

def category(request):
    return render(request, 'admin/categories.html')

def products(request):
    products = Product.objects.all()  # or whatever query you're using
    return render(request, 'admin/products.html', {'products': products})


def productimage(request):
    return render(request, 'admin/productimages.html')

def sizevariant(request , slug):
        product = Product.objects.get(slug =slug)
        return render(request  , 'admin/sizevariant.html' , context = {'product' : product})


def colorvariant(request):
    return render(request, 'admin/colorvariant.html')

def createproduct(request):
    return render(request, 'admin/createproduct.html')
