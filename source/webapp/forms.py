from django import forms
from .models import Product


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')

