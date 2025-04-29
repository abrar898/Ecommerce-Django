# from django.db import models
# from django.contrib.auth.models import User
# from products.models import Product

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming each cart is associated with a user
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True) 

#     def __str__(self):
#         return f"Cart {self.id} for {self.user.username}"


# class CartItems(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)  # Store quantity of the product in the cart

#     def __str__(self):
#         return f"{self.quantity} x {self.product.product_name}"
    
#     @property
#     def total_price(self):
        # return self.quantity * self.product.price  # Calculate total price for this cart item

