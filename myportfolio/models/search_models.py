from django.db import models
from .const import MAX_LENGTH_TICKER_SYMBOL

class SearchHistory(models.Model):

    symbol = models.CharField(max_length=MAX_LENGTH_TICKER_SYMBOL)
    sell  = models.IntegerField(default = 0)
    neutral  = models.IntegerField(default = 0)
    buy  = models.IntegerField(default = 0)
    price = models.FloatField(default = 0.0)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symbol
    
    class Meta:
        verbose_name = "Search History"
        verbose_name_plural = "Search History Entries"  # Optional, for plural form
