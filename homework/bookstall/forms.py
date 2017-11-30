from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import *


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             widget=forms.widgets.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Фамилия'}))
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Логин'}))
    password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True,
                                widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Подтверждение пароля'}))

    class Meta:
        fields = [
            'email',
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]
        model = User


class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Пароль'}))