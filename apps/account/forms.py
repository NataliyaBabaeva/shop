from typing import Any
from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.template.defaultfilters import slugify



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'type':'password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'type':'password'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        
    # widgets ={
    #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder' :' enter username','type':'text'}),
    #     'password': forms.PasswordInput(),
    #     'password2': forms.PasswordInput(),
    # }   
        
    def clean(self) :
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise ValidationError({'password':'Password mismatch '})
        if len(password)<8:
            raise ValidationError({'password':'Password must contain at least 8 characters'})
        
        
class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'type':'text'}))
    
    password = forms.CharField(widget = forms.PasswordInput(attrs={'type':'password'}))
    
    
    
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
        
        
    
    
        
        








