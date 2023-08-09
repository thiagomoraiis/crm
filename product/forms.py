from django import forms
from .models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name', 'price', 'description',
            'stock', 'image', 'category',
            'tags'
        )
