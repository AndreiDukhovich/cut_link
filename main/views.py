from django.shortcuts import  render, redirect
from .models import Users_link
from django.contrib.auth.decorators import login_required
from .services import *

@login_required
def list(request):
    '''Show user all his links.'''
    user_links = get_user_links(request)
    return render(request, 'main/list.html', {'links': user_links})

@login_required
def create_cut_link(request):
    '''Create record about long and cut link.'''
    data = get_all_data_for_create_cut_link(request)
    return render(request, 'main/main.html', data)

@login_required
def redir(request, link):
    '''Redirect user to site via short link.'''
    long_link = get_long_link_from_cut_link(request=request, link=link)
    return redirect(long_link) 

def registration(request):
    '''Registration user.'''
    data = get_all_data_for_registration_view(request)
    return render(request, 'registration/createUser.html', data)

def loginplease(request):
    '''View for not login users.'''
    return render(request, 'loginplease.html')