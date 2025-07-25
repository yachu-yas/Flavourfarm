from django.db import models
from base.models import Base_Model

# Create your models here.
class Product(Base_Model):
    # Other fields...
    is_offer = models.BooleanField(default=False)
    is_top_selling = models.BooleanField(default=False)

    def __str__(self):
        return self.name
