from django.urls import path
from products.views import get_product ,buy_now,category_filter,create_product, update_product, delete_product, product_list, add_product, add_color, add_size, add_category
urlpatterns = [
    # Specific routes first
    path('add/', add_product, name='add_product'),
    path('add-color/', add_color, name='add_color'),
    path('add-size/', add_size, name='add_size'),
    path('add-category/', add_category, name='add_category'),
    path('product/category/<slug:category_slug>/', category_filter, name='category_filter'),
    path('buy/<int:id>/', buy_now, name='buy_now'),
    path('products/', product_list, name='product_list'),
    path('products/create/', create_product, name='create_product'),
    path('products/update/<int:product_id>/', update_product, name='update_product'),
    path('products/delete/<int:product_id>/', delete_product, name='delete_product'),
    
    # Catch-all slug pattern must be last
    path('<slug>/' , get_product , name="get_product"),
]


