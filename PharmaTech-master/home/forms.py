from django import forms 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control','placeholder':'Enter Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
     

class LogIn(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control','placeholder':'Enter Username'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
   
    class Meta:
        model = User
        fields = ['username','password']


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# # Create a UserUpdateForm to update a username and email
# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']

# # Create a ProfileUpdateForm to update image.
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']


   