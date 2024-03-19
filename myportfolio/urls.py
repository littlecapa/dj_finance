# myportfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chess/', views.chess, name='chess'),
]

