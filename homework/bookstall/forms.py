from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import *
from .models import *


class UserCreateForm(UserCreationForm):
    email = EmailField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}))
    first_name = CharField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = CharField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Фамилия'}))
    username = CharField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Логин'}))
    password1 = CharField(required=True, widget=widgets.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = CharField(required=True, widget=widgets.PasswordInput(attrs={'placeholder': 'Подтверждение пароля'}))

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

    username = CharField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Логин'}))
    password = CharField(required=True, widget=widgets.PasswordInput(attrs={'placeholder': 'Пароль'}))


class BookForm(ModelForm):
    title = CharField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Название'}))
    image = ImageField(required=True)
    year = IntegerField(required=True, widget=widgets.NumberInput(attrs={'placeholder': 'Год издания'}))
    count = IntegerField(required=True, widget=widgets.NumberInput(attrs={'placeholder': 'Количество'}))

    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(ModelForm):
    first_name = CharField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = CharField(required=True, widget=widgets.TextInput(attrs={'placeholder': 'Фамилия'}))

    class Meta:
        model = Author
        fields = '__all__'