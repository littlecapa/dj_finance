# myportfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chess/', views.chess, name='chess'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('es/', views.es, name='es'),
    path('links/', views.links, name='links'),
    path('playground/', views.playground, name='playground'),
    path('detail/', views.detail, name='detail'),
    path('tradingview/', views.tradingview, name='tradingview'),
    path('tradingview/<str:ticker>/', views.tradingview, name='tradingview'),
    path('search/', views.search_view, name='search'),
]

handler404 = views.chess