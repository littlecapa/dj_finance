# myportfolio/views.py
import json
from django.shortcuts import render
from .models import MainShares, Category, Link

def home(request):
    stocks = MainShares.objects.all()
    # Construct the symbol_string
    symbols = [[stock.name, stock.symbol] for stock in stocks]
    context = {'main' : json.dumps(symbols)}
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
    # Get all categories
    categories = Category.objects.all()
    print(categories)

    # Pass categories and associated links to the template
    categories_with_links = []
    for category in categories:
        # Get links associated with the current category
        links = Link.objects.filter(category=category)
        if links.count() > 0:
            categories_with_links.append({'category': category, 'links': links})
    #print(categories_with_links)
    return render(request, 'myportfolio/links.html', {'categories': categories_with_links})

def playground(request):
    data = ''' "symbols": [
					  {
						"description": "",
						"proName": "NASDAQ:TSLA"
					  },
					  {
						"description": "",
						"proName": "NASDAQ:AAPL"
					  },
					  {
						"description": "",
						"proName": "NASDAQ:NVDA"
					  },
					  {
						"description": "",
						"proName": "NASDAQ:MSFT"
					  },
					  {
						"description": "",
						"proName": "NASDAQ:AMZN"
					  },
					  {
						"description": "",
						"proName": "NASDAQ:GOOGL"
					  },
					  {
						"description": "",
						"proName": "NASDAQ:META"
					  },
					  {
						"description": "",
						"proName": "NYSE:BRK.B"
					  },
					  {
						"description": "",
						"proName": "NYSE:LLY"
					  },
					  {
						"description": "",
						"proName": "NYSE:UNH"
					  },
					  {
						"description": "",
						"proName": "NYSE:V"
					  },
					  {
						"description": "",
						"proName": "NYSE:WMT"
					  }
					],
					"showSymbolLogo": true,
					"colorTheme": "light",
					"isTransparent": false,
					"displayMode": "adaptive",
					"locale": "en"
					 }]'''
    return render(request, 'myportfolio/playground.html', {'data': data})

def tradingview(request):
    symbols = [
        {"description": "", "proName": "NASDAQ:TSLA"},
        {"description": "", "proName": "NASDAQ:AAPL"},
        {"description": "", "proName": "NASDAQ:NVDA"},
        # Add more symbols as needed
    ]
    return render(request, 'myportfolio/tradingview_master.html', {'symbols': symbols})
