from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Product



def shop_all_products(request):
    if request.GET.get("header_search"):
        user_input = request.GET.get("header_search")
        products = Product.objects.filter(name__icontains=user_input)
    else:
        products = Product.objects.all()

    context = {
        "products": products
    }
    return render(request, "products/allProducts.html", context)


def view_product_from_category(request, slug):
  
        
    products = Product.objects.filter(category__slug = slug)
    context = {
        "products" : products
    }
    return render (request,"products/allProducts.html",context)

   

def view_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {
            "product": product
        }
        return render(request, "products/viewProduct.html", context)
    except Product.DoesNotExist:
        messages.error(request, "Product not found.")
        return redirect("shop_all_products")
