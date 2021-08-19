from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser


User = get_user_model()

#Log in Form
class LoginForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password1',
            ]


# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    
    role = forms.CharField(max_length=30, required=False)
    company = forms.CharField(max_length=30, required=False)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'role', 
            'company', 
            'password1', 
            'password2', 
            ]


# Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'role', 
            'company',
            ]
