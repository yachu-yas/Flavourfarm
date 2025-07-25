from django.db import models

# Create your models here.
# cart/models.py
from django.contrib.auth.models import User
from products.models import Product  # Assuming the product model is in the 'products' app

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    is_active = models.BooleanField(default=True)  # Track if the cart is active or not

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)  # One cart can have multiple items
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # One cart item is linked to one product
    quantity = models.PositiveIntegerField(default=1)  # How many of the product the user wants to buy

    def __str__(self):
        return f"{self.product.name} - {self.quantity} items"
