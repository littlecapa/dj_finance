# myportfolio/views.py

from django.shortcuts import render

def home(request):
    context = {'input_symbol': 'AAPL'}
    return render(request, 'myportfolio/home.html', context)

def chess(request):
    context = {}
    return render(request, 'myportfolio/chess.html', context)

def portfolio(request):
    context = {}
    return render(request, 'myportfolio/construction.html', context)

def es(request):
    context = {}
    return render(request, 'myportfolio/construction.html', context)

def links(request):
    context = {}
    return render(request, 'myportfolio/construction.html', context)



