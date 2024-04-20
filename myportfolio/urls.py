# myportfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('chess/', views.chess, name='chess'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('es/', views.es, name='es'),
    path('links/', views.links, name='links'),
    path('playground/', views.playground, name='playground'),
    path('detail/', views.detail, name='detail'),
    path('tradingview/', views.tradingview, name='tradingview'),
    path('tradingview/<str:ticker>/', views.tradingview, name='tradingview'),
    path('search/', views.search_view, name='search'),
    path('share-ids-popup/', views.share_ids_popup, name='share_ids_popup'),
    path('blog/', views.blog, name='blog'),
    path('test/', views.test, name='test'),
    path('process_stocks/<int:pk>/', views.process_stocks_view, name='process_stocks'),
    path('text2stocks/', views.text2stocks, name='text2stocks'),
]

handler404 = views.chess