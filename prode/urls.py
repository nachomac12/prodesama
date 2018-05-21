from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'prode'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', auth_views.login, {'template_name': 'prode/login.html'} )
] 