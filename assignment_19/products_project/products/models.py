from django.db import models

from products.choices import PRODUCT_CATEGORIES


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='product name')
    category = models.IntegerField(choices=PRODUCT_CATEGORIES, verbose_name='product category')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='product price')

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
