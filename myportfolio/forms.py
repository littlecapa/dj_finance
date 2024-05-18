from django import forms
from django.contrib import admin
from .models import shareIds, blogEntry, sourceChoices

class CSVUploadForm(forms.Form):
    method = forms.ChoiceField(choices=sourceChoices, widget=forms.Select)
    csv_file = forms.FileField(label='Select local CSV file')

class SearchForm(forms.Form):
    symbol = forms.CharField(label="Ticker Symbol", max_length=20, required=False)
    wkn = forms.CharField(label="WKN", max_length=8, required=False)

class ShareIdsPickerForm(forms.ModelForm):
    shareInfos = forms.ModelMultipleChoiceField(
        queryset=shareIds.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple(verbose_name='Share IDs', is_stacked=False),
    )

class BlogEntryAdminForm(forms.ModelForm):
    class Meta:
        model = blogEntry
        exclude = ('stocksProcessed',)