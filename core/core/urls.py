from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from shop.views import home, contact_page
from products.views import shop_all_products, view_product, view_product_from_category
from payments.views import payment_sucess
from user_profile.views import user_registration, user_login, user_logout, orders, add_to_cart, user_cart, remove_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),

    # Store and product pages
    path('', home, name='home'),
    path('shop', shop_all_products, name='shop_all_products'),
    path('<str:slug>', view_product, name='view_product'),
    path('category/<str:slug>', view_product_from_category, name='category'),

    # User auth and orders
    path('user/registration', user_registration, name='user_registration'),
    path('user/login', user_login, name='user_login'),
    path('user/logout', user_logout, name='user_logout'),
    path('user/order', orders, name='user_order'),

    # Cart and checkout
    path('user/cart', user_cart, name='view_cart'),
    path('user/add-to-cart/<int:product_id>/<int:quantity>', add_to_cart, name='user_add_to_cart'),
    path('user/remove-from-cart/<int:item_id>', remove_from_cart, name='remove_from_cart'),
    path('user/checkout/success/', payment_sucess, name='payment_sucess'),

    # Contact
    path('shop/contact', contact_page, name='contact_page'),

    # Optional: include more if needed
    path('cart/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
