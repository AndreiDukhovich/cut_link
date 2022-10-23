from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import urllib3

def url_validation(url):
    http = urllib3.PoolManager()
    try:
        resp = http.request('GET', url)
    except:
        raise forms.ValidationError('Данного адреса не существует')

class Links_form(forms.Form):
    name = forms.CharField(label='Имя ссылки',
        widget=forms.TextInput(attrs={"class":"myfield", 'placeholder': 'Введите имя ссылки'}))

    long_link = forms.URLField(label='', validators=[url_validation],
        widget=forms.TextInput(attrs={'class': 'formText', 'placeholder': 'Введите ссылку'}))
        

class RegistrationUser(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
        widget=forms.TextInput(attrs={"class":"myfield"}))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"myfield"}))

    last_name = forms.CharField(label='Фамилия', required=True, widget=forms.TextInput(attrs={"class":"myfield"}))
    
    first_name = forms.CharField(label='Имя', required=True, widget=forms.TextInput(attrs={"class":"myfield"}))

    password1 = forms.CharField(label='Пароль:', required=True,
        help_text=['Пароль не должен быть слишком похож на другую вашу личную информацию.',
                    'Ваш пароль должен содержать как минимум 8 символов.',
                    'Пароль не может состоять только из цифр.'],
        widget=forms.PasswordInput(attrs={"class":"myfield"}))

    password2 = forms.CharField(label='Подтверждение пароля:', required=True,
        widget=forms.PasswordInput(attrs={"class": "myfield"}))


    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password1', 'password2']