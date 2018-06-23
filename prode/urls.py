from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views
from .models import Bet

app_name = 'prode'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', auth_views.login, {'template_name': 'prode/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', login_required(views.HomeView.as_view()), name='home'),
    path('home/apuestas', login_required(views.BetView.as_view()), name='apuestas'),
    path('home/datos', login_required(views.MyDataView.as_view()), name='datos'),
    path('home/puntaje', login_required(views.ScoreView.as_view()), name='puntaje'),
    # path('home/grupos', login_required(views.GroupView.as_view()), name='grupos'),
    ] 
