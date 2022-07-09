from os import curdir
from django.shortcuts import render, redirect
from .models import Users_link
from .forms import Links_form, RegistrationUser
from random import choice
from string import ascii_letters
from django.contrib.auth import authenticate, login

def get_cut_link(request):
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



# Create your views here.
def list(request):
    links = Users_link.objects.filter(user=request.user)
    return render(request, 'main/list.html', {'links': links})


def main(request):
    error = ''
    cut_link = ''
    if request.method == 'POST':
        form = Links_form(request.POST)
        new_note = form.save(commit=False)
        new_note.user = request.user
        cut_link = get_cut_link(request)
        new_note.cut_link = cut_link
        new_note.save()
        if form.is_valid():
            form.save()
        else:
            error = 'Ой, что-то не так.'
    form = Links_form()
    data = {'form': form, 'error': error, 'cut_link': cut_link}
    return render(request, 'main/main.html', data)

def redir(request, link):
    long_link = Users_link.objects.get(cut_link='http://' + request.get_host() + '/' +link)
    return redirect(long_link) 

def registration(request):
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
    data = {'form': form}
    return render(request, 'registration/createUser.html', data)
