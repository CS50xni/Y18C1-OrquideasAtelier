
from django import forms
# from django.core.validators import MaxValueValidator, MinValueValidator

#PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1, 15)]

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField( min_value=0)
    #quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
