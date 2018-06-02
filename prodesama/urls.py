from django.contrib import admin
from django.urls import path, include
from prode import views as prodeViews

urlpatterns = [
    path('', include('prode.urls')), 
    path('admin/', admin.site.urls),
    path('accounts/profile/', prodeViews.BetView.as_view(), name='home'),
]
