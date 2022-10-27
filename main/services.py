from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.db import IntegrityError
import qrcode
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404, redirect
from .forms import Links_form, RegistrationUser
from random import choice
from string import ascii_letters
from .models import Users_link
from django.core.files import File
from django.contrib.auth import authenticate, login

def create_qr_code(link : str, file_name : str) -> File:
    '''Create qr-code for shot link and return it image.'''
    data = link
    filename = f"{file_name}.png"
    img = qrcode.make(data)
    img.save('static\\qr\\'+filename)
    return File(open('static\\qr\\'+filename, 'rb'))


def get_cut_link(request: WSGIRequest) -> str:
    '''Take HTTP-request and return short url
    consisting of 6 symbols.'''
    cut_link = ''
    simbols = ascii_letters + '0123456789'
    cut_link_list = Users_link.objects.values_list('cut_link', flat=True)
    while True:
        for _ in range(6):
            cut_link += choice(simbols)
        if cut_link in cut_link_list:
            cut_link = ''
        else:
            break
    return 'http://' + request.get_host() + '/' + cut_link


def get_user_links(request: WSGIRequest) -> QuerySet:
    '''Return user links.'''
    return Users_link.objects.filter(user=request.user)

def get_all_data_for_create_cut_link(request: WSGIRequest)-> dict:
    '''Get data that need send to user for create cut link.'''
    mes = ''
    if request.method == 'POST':
        is_success_or_link = _create_cut_link(request=request)
        if is_success_or_link: 
            html_link = f'<a href={is_success_or_link.cut_link}>{is_success_or_link.cut_link}</a>'
            mes = mark_safe(f'Ваша короткая ссылка: {html_link}')
        else:
            mes = 'Проверте введенные данные'
    form = Links_form()
    return {'form': form, 'mes': mes}

def _create_cut_link(request: WSGIRequest) -> bool | Users_link:
    '''Take HTTP-request and try create Users_link object. If object is create, return it.
    If not return False'''
    form = Links_form(request.POST)
    if form.is_valid():
        data_for_creat_cut_link = _get_data_for_create_cut_link(request=request,
            request_data=form.cleaned_data)
        return _get_link_data_if_create_or_false(data_for_creat_cut_link)
    return False

def _get_data_for_create_cut_link(request: WSGIRequest, request_data: dict) -> dict:
    '''Return dictionary for create User_link object.'''
    long_link = request_data.get('long_link')
    name = request_data.get('name')
    cut_link = get_cut_link(request)
    return {'user': request.user, 'long_link': long_link, 
        'name': name, 'cut_link': cut_link}

def _get_link_data_if_create_or_false(data: dict) -> bool:
    '''Take data for create User_link object and create it.
    Return User_link object if it is create or False'''
    try:
        link_data = Users_link.objects.create(user=data['user'], name=data['name'], 
                long_link=data['long_link'], cut_link=data['cut_link'], 
                qr=create_qr_code(link=data['cut_link'], file_name=data['name']))
    except IntegrityError:
        return False
    return link_data


def get_all_data_for_registration_view(request: WSGIRequest) -> dict:
    '''Get data that need send to user for registration.'''
    if request.method == 'POST':
        form = RegistrationUser(request.POST)
        if form.is_valid():
            u_name = form.cleaned_data.get('username')
            u_pass = form.cleaned_data.get('password2')
            form.save()
            user = authenticate(username=u_name,
                                password=u_pass)
            login(request, user)
            return redirect('main')
    form = RegistrationUser()
    return {'form': form}


def get_long_link_from_cut_link(request: WSGIRequest, link: str) -> str:
    '''Take cut link and return long link.'''
    return get_object_or_404(Users_link, 
        cut_link='http://' + request.get_host() + '/' +link).long_link