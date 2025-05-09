"""coffeeshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from .import views
# from products.views import category_filter

urlpatterns = [
    path('' , include('home.urls') ),
    # path('jet',include(('jet.urls'),'jet')),
    # path('jet',include(('jet.urls'),'jet')),
    # path('jet/dashboard/',include(('jet.dashboard.urls'),'jet-dashboard')),
    path('product/' , include('products.urls') ),
    # path('coffee/' , include('coffee.urls') ),
    # path('category/<slug:category_slug>/', category_filter, name='category_filter'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('accounts/' , include('accounts.urls') ),
    path('hydr/' , include('hydr.urls') ),
    path('cart/' , include('cart.urls') ),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()