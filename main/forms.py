from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, CharField, EmailField, EmailInput, PasswordInput
from .models import Users_link

class Links_form(ModelForm):
    long_link = CharField(label='', widget=TextInput(attrs={'class': 'formText', 'placeholder': 'Введи ссылку'}))
    class Meta:
        model = Users_link
        fields = ['long_link']
        

class RegistrationUser(UserCreationForm):
    username = CharField(label='Имя пользователя',
                               widget=TextInput(attrs={"class":"myfield"}))
    email = EmailField(required=True, widget=EmailInput(attrs={"class":"myfield"}))
    last_name = CharField(label='Фамилия', required=True, widget=TextInput(attrs={"class":"myfield"}))
    first_name = CharField(label='Имя', required=True, widget=TextInput(attrs={"class":"myfield"}))
    password1 = CharField(label='Пароль:', required=True,
                                help_text=['Пароль не должен быть слишком похож на другую вашу личную информацию.',
                                'Ваш пароль должен содержать как минимум 8 символов.',
                                'Пароль не может состоять только из цифр.'],
                                widget=PasswordInput(attrs={"class":"myfield"}))
    password2 = CharField(label='Подтверждение пароля:', required=True,
                                widget=PasswordInput(attrs={"class": "myfield"})
                                )
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password1', 'password2']