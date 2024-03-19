# myportfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chess/', views.chess, name='chess'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('es/', views.es, name='es'),
    path('links/', views.links, name='links'),
]

