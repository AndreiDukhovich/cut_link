from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('', views.main, name='main'),
    path('<str:link>', views.redir, name='redirect'),
    path('loginplease/', views.loginplease, name='loginplease'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/registration', views.registration, name='registration'),
]