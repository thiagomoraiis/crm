from django import forms
from .models import CustomUser


class UserRegisterModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'telephone', 'city', 'address',
            'office', 'password'
        )
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
            'telephone': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'city': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'address': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'office': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control'}
            ),
        }
