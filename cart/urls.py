from django.urls import path
from .views import cart_add, cart_detail, checkout, cart_remove

urlpatterns = [
    path('cart/add/<slug:slug>/', cart_add, name='cart_add'),
    path("cart_detail", cart_detail, name="cart_detail"),
    path("checkout", checkout, name="checkout"), 
    path("remove/<slug:slug>/", cart_remove, name="cart_remove")
]
