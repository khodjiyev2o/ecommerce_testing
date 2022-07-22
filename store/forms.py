from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['name', 'price', 'digital','image']:
            self.fields[fieldname].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Product                                                                       
        fields = '__all__'
