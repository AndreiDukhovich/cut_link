from django.shortcuts import get_object_or_404, render, redirect
from .models import Users_link
from .forms import Links_form, RegistrationUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .services import *

@login_required
def list(request):
    links = Users_link.objects.filter(user=request.user)
    return render(request, 'main/list.html', {'links': links})

@login_required
def main(request):
    error = ''
    cut_link = ''
    if request.method == 'POST':
        form = Links_form(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('long_link')
            name = form.cleaned_data.get('name')
            cut_link = get_cut_link(request, link)
            Users_link.objects.create(user=request.user, name=name, 
            long_link=link, cut_link=cut_link, 
            qr=create_qr_code(link=link, file_name=name))
        else:
            error = 'Проверте правильность ввода ссылки.'
    form = Links_form()
    data = {'form': form, 'error': error, 'cut_link': cut_link}
    return render(request, 'main/main.html', data)

@login_required
def redir(request, link):
    long_link = get_object_or_404(Users_link, cut_link='http://' + request.get_host() + '/' +link).long_link
    print(long_link)
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

def loginplease(request):
    return render(request, 'loginplease.html')