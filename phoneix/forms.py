
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    state = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'state', 'password1', 'password2']







