from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from base.models import Base_Model

# Product Category
class Product_Category(Base_Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to="Product_Category_Images", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product_Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# Product Manufacturer
class Product_Manufacturer(Base_Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

# Product Brand
class Product_Brand(Base_Model):
    manufacturer = models.ForeignKey(Product_Manufacturer, on_delete=models.CASCADE, related_name="brands")
    name = models.CharField(max_length=128, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

# Product
class Product(Base_Model):
    category = models.ForeignKey(Product_Category, on_delete=models.CASCADE, related_name="products")
    manufacturer = models.ForeignKey(Product_Manufacturer, on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(Product_Brand, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    retail_price = models.FloatField(validators=[MinValueValidator(0.0)])
    selling_price = models.FloatField(validators=[MinValueValidator(0.0)])
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    slug = models.SlugField(unique=True, null=True, blank=True)
    is_offer = models.BooleanField(default=False)  # New field for offer products
    is_top_selling = models.BooleanField(default=False)  # New field for top-selling products

    def discount_percentage(self):
        if self.retail_price > 0:
            return round(((self.retail_price - self.selling_price) / self.retail_price) * 100)
        return 0

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# Product Images
class ProductImage(Base_Model):
    for_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="Product_Images")

    def __str__(self):
        return self.for_product.name
