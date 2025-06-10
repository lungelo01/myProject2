from django.urls import path
from . import views


"""Roots the view 'details' to the url.py file

"""

app_name = "polls"
urlpatterns = [
    path('<int:question_id>/detail/', views.detail, name='detail'),
    path('index/', views.index, name='index'),
]
