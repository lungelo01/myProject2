from django.urls import path
from . import views

"""roots 'view' and 'home' to the urls.py file

"""
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
]
