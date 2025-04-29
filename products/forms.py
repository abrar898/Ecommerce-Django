from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'price', 'product_description', 'color_variant', 'size_variant']
        widgets = {
            'color_variant': forms.CheckboxSelectMultiple(),
            'size_variant': forms.CheckboxSelectMultiple(),
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
