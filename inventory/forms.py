from .models import Product
from django import forms
from django.core.validators import RegexValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class ProductForm(forms.ModelForm):

    product_SKU = forms.CharField(label="Product SKU", validators=[RegexValidator(
        r'^[0-9a-zA-Z]+$', 'Only alphanumeric characters are allowed for the SKU.')])
    product_weight = forms.FloatField(help_text="Enter product weight in grams.", validators=[
                                      MinValueValidator(0, "Weight cannot be negative.")])

    class Meta:
        model = Product
        fields = "__all__"
