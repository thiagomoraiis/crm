from django import forms
from product.models import Inventory


class InventoryModelForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('product', 'quantity')
