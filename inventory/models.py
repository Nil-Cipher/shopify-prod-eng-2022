import datetime
from django.urls import reverse
from django.db import models
from django.utils import timezone


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_count = models.PositiveIntegerField()
    product_SKU = models.CharField(max_length=30)
    product_weight = models.FloatField()

    def __str__(self):
        return self.product_name

    # Metadata
    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Product."""
        return reverse('inventory:product-detail', args=[str(self.id)])
