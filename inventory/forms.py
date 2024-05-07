from django import forms
from .models import Product, ProductSubImage, Product, ProductTag
from django.forms import inlineformset_factory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  

class ProductSubImageForm(forms.ModelForm):
    class Meta:
        model = ProductSubImage
        fields = '__all__'  

 
class ProductTagInlineForm(forms.ModelForm):
    class Meta:
        model = ProductTag
        fields = ['tagname', 'tag', 'has_color']
        widgets = {
            'tag': forms.Select(attrs={'class': 'form-control'}),
            'tagname': forms.TextInput(attrs={'class': 'form-control'}),
            'has_color': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# Use ProductTag as the model for inline formset
ProductTagInlineFormSet = inlineformset_factory(
    Product,
    ProductTag,
    form=ProductTagInlineForm,
    fields=('tagname', 'tag', 'has_color'),
    extra=1,
    can_delete=False,
    min_num=1,
    validate_min=True,
)