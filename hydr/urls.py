from django.urls import path
from hydr.views import user, home,category,products ,sizevariant ,colorvariant ,profiles



urlpatterns = [
    path('user/' , user , name="user"),
    path('admin1/' , home , name="admin1"),
    path('categories/' , category , name="categories"),
    path('products/' , products , name="products"),
    path('products/' , products , name="products"),
    path('sizevariant/<slug>/', sizevariant, name="sizevariant"),
    path('colorvariant/' ,colorvariant , name="colorvariant"),   
    path('profiles/' ,profiles , name="profiles"),    
     
        
]