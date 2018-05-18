from django.urls import path

from . import views

app_name = 'prode'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]