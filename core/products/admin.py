from django.contrib import admin
#from .models import Product, Product_Images, Product_Category, Product_Manufacturer, Product_Brand
from .models import Product, ProductImage, Product_Category, Product_Manufacturer, Product_Brand


class ProductImagesInline(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    list_display = ["name", "category", "retail_price", "selling_price", "stock", "discount_percentage"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Category)
admin.site.register(Product_Manufacturer)
admin.site.register(Product_Brand)
