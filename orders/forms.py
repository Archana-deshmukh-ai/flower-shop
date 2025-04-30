from django import forms
from .models import OrderCustomization

class CustomizationForm(forms.ModelForm):
    class Meta:
        model = OrderCustomization
        fields = ['ribbon_type', 'ribbon_color', 'custom_message']
