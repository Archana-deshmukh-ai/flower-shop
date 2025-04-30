from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# from .models import Customization

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User   
        fields = ['username', 'email', 'password1', 'password2']

# class CustomizationForm(forms.ModelForm):
#     class Meta:
#         model = Customization
#         fields = ['field_name_1', 'field_name_2']  




