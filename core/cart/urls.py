from django.urls import path
from user_profile.views import user_cart, add_to_cart, remove_cart_items, check_out

urlpatterns = [
    path('cart', user_cart, name='user_cart'),
    path('add-to-cart/<str:u_id>/<int:qty>', add_to_cart, name='cart_add_to_cart'),
    path('remove-from-cart/<str:u_id>', remove_cart_items, name='remove_cart_items'),
    path('checkout/<str:cart_id>', check_out, name='check_out'),
]
