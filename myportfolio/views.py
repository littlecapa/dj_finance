# myportfolio/views.py

from django.shortcuts import render

def home(request):
    context = {'input_symbol': 'AAPL'}
    return render(request, 'myportfolio/home.html', context)

def chess(request):
    context = {}
    return render(request, 'myportfolio/chess.html', context)
