from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Product_Category, Product_Manufacturer, Product_Brand

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "retail_price", "selling_price", "image_tag", "stock", "discount_percentage"]

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover;" />', obj.image.url)
        return "-"
    image_tag.short_description = "Image"

admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Category)
admin.site.register(Product_Manufacturer)
admin.site.register(Product_Brand)
