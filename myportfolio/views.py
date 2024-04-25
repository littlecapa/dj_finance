# myportfolio/views.py
import json
import urllib.parse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.safestring import mark_safe
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Category, Link, shareIds, blogEntry
from .forms import SearchForm
from .libs.tradeview_info import save_search_history, EXCEPTION_SymbolNotFound
from .libs.text2stocks import extract_stocks, saveBlogStocks

def text2stocks(request):
    blog_id = request.GET.get('blog_id')
    headline = request.GET.get('headline')
    ref_stocks = request.GET.get('ref_stocks')
    shares = extract_stocks(ref_stocks)
    data = {'blog_id': blog_id, 'headline': headline, "ref_stocks": ref_stocks, "shares": shares, "return_url": "/myportfolio/savestocks/"}
    # Serialize the data to JSON format
    json_data = json.dumps(data)
    response = HttpResponse(json_data, content_type='application/json', status=200)
    return response

def save_blog_stocks(request):
    if request.method == "GET":
        response = request.GET['response']
        saveBlogStocks(response)
    response = HttpResponse(status=200)
    return response

def done(request):
    return redirect('/myportfolio/home/')

def blog(request):
    context = {}
    return render(request, 'myportfolio/blog.html', context)

def process_stocks_view(request, pk):
    # Retrieve the blogEntry based on the provided pk
    blog_entry = get_object_or_404(blogEntry, pk=pk)
    context = {"blog_id": pk, "headline": blog_entry.headLine, "stocks": blog_entry.referencedStocks}
    return render(request, 'myportfolio/process_stocks.html', context)

def share_ids_popup(request):
    share_ids = shareIds.objects.all()
    return render(request, 'myportfolio/shareids_popup.html', {'share_ids': share_ids})

def home(request):
    stocks = shareIds.objects.filter(isMainShare=True)
    stocks_data = [{'proName': stock.symbol, 'title': stock.name} for stock in stocks]
    # Serializing the extracted data
    stocks_json = mark_safe(json.dumps(stocks_data))
    return render(request, 'myportfolio/home.html', {"symbol_list": stocks_json})

def test(request, exception = None):
    context = {}
    return render(request, 'myportfolio/test.html', context)

def chess(request, exception = None):
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
    symbol = "NASDAQ:AAPL"
    symbol_list = [
        {"proName": "NASDAQ:AAPL", "title": "Apple"},
        {"proName": "NASDAQ:GOOGL", "title": "Alphabet"}
    ]  
    return render(request, 'myportfolio/playground.html', {'input_symbol': symbol, 'width': '50%', "symbol_list": mark_safe(json.dumps(symbol_list))})

def detail(request):
    symbol = "NASDAQ:AAPL"
    return render(request, 'myportfolio/detail.html', {'input_symbol': symbol})

def tradingview(request,ticker = 'AAPL'):
    try:
        save_search_history(ticker)
    except EXCEPTION_SymbolNotFound:
        pass
    symbol_descr = [
        {"description": "", "proName": "NASDAQ:TSLA"},
        {"description": "", "proName": "NASDAQ:AAPL"},
        {"description": "", "proName": "NASDAQ:NVDA"},
        # Add more symbols as needed
    ]
    symbol_list = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN', 'FB']
    return render(request, 'myportfolio/tradingview_master.html', {'symbol_list': symbol_list, 'ticker': ticker})

def search_view(request):
    form = SearchForm(request.GET)
    search_results = None

    if form.is_valid():
        ticker_symbol = form.cleaned_data.get('ticker_symbol')
        wkn = form.cleaned_data.get('wkn')

        if ticker_symbol and wkn:
            # Display an error message to the user
            error_message = "Please fill out only one field."
            return render(request, 'search.html', {'form': form, 'error_message': error_message})

        if wkn:
            # Call the microservice to identify the ticker symbol based on WKN
            # Example:
            # search_results = call_microservice(wkn)
            pass
        elif ticker_symbol:
            target_url = f'/tradingview/{ticker_str}/'
            return redirect(target_url)
    
    return render(request, 'myportfolio/search.html', {'form': form, 'search_results': search_results})
