from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="products", default="default_product.png")
    price = models.FloatField(help_text='in US Dollars $')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}-{self.created_at.strftime('%d/%m/%Y')}"
