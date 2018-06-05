from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'prode'
urlpatterns = [
    path('', views.MatchView.as_view(), name='index'),
    path('login/', auth_views.login, {'template_name': 'prode/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.BetView.as_view(), name='home'),
    ] 
