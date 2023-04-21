from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-label border border-black"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-label border border-black"
    }))
    
class SignupForm(UserCreationForm):
    class Meta:   
        model = User
        fields = ("username","email","password1","password2")

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-label border border-black"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class":"form-label border border-black"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-label border border-black"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-label border border-black"
    }))