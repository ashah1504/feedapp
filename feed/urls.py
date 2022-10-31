
from django.contrib import admin
from django.urls import path, include

from feedapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feedapp.urls')),
    path('', include('social_django.urls')),
    path('logout/', views.logout, name='logout'),
]
