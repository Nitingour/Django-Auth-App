from django import forms
from django.contrib.auth.models import User
from BlogApp.models import Blog
class SignupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password','email','first_name','last_name')


class BlogForm(forms.ModelForm):
    description=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Blog
        fields=('title','description','image',)
