from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('prode/', include('prode.urls')), 
    path('admin/', admin.site.urls),
]
