from django.forms import ModelForm, TextInput, Select, NumberInput, FileInput, Textarea, ModelChoiceField
from .models import Product, Category


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'is_negotiable',
            'condition',
            'post_category',
            'location',
            'details',
            'author',
            'phone',
            'category'

        ]
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
                   'price': NumberInput(attrs={'class': 'form-control', 'placeholder': '$'}),
                   'condition': Select(attrs={'class': 'form-control', 'placeholder': '$'}),
                   'category': Select(attrs={'class': 'form-control'}),
                   'location': Select(attrs={'class': 'form-control'}),
                   'post_category': Select(attrs={'class': 'form-control', 'placeholder': '$'}),
                   'phone': TextInput(attrs={'class': 'form-control', 'placeholder': '017000000'}),
                   'author': TextInput(attrs={'class': 'form-control', 'type': 'hidden', 'value': '{{ request.user.id}}'}),
                   'details': Textarea(attrs={'class': 'form-control', 'rows': "3",
                                               'placeholder': 'ex: 256GB, Color: Royal Blue, Battery: 88%;'}),
                   }

