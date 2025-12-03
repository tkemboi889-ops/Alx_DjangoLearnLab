from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

#creating a profile update form

class UpdateUserForm(UserChangeForm):
    password = None  # Hide password field

    class Meta:
        model = User
        fields = ["username", "email"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  
