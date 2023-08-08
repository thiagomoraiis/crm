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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(self, *args, **kwargs)
#
    #    for field_name, field in self.fields.items():
    #        field.widgets.attrs['class'] = 'form-control'
