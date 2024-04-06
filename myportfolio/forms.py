from django import forms

class SearchForm(forms.Form):
    symbol = forms.CharField(label="Ticker Symbol", max_length=20, required=False)
    wkn = forms.CharField(label="WKN", max_length=8, required=False)