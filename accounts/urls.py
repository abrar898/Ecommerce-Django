from django.urls import path
from accounts.views import  login,register, reset_admin_password
from products.views import add_to_cart ,cart_view
urlpatterns = [
   path('login/' , login , name="login" ),
   path('register/' , register , name="register"),
   path('reset-password/', reset_admin_password, name="reset_password"),
   # path('activate/<email_token>/' , activate_email , name="activate_email"),
   path('add-to-cart/<uid>/',add_to_cart,name="add_to_cart"),
   path('cart/', cart_view, name='cart'),
]
