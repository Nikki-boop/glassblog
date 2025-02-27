
from django import forms
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'date_posted', 'author', 'topic', 'image']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']