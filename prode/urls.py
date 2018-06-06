from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'prode'
urlpatterns = [
    path('', views.MatchView.as_view(), name='index'),
    path('login/', auth_views.login, {'template_name': 'prode/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', login_required(views.HomeView.as_view()), name='home'),
    path('home/apuestas', views.BetView.as_view(), name='apuestas'),
    path('home/datos', views.MyDataView.as_view(), name='datos'),
    path('home/puntaje', views.ScoreView.as_view(), name='puntaje'),
    path('home/grupos', views.GroupView.as_view(), name='grupos'),
    ] 
