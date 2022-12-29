from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ['username','password1','password2']

