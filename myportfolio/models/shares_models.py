from django.db import models
from .const import MAX_LENGTH_TICKER_SYMBOL, MAX_LENGTH_WKN, MAX_LENGTH_ISIN

class shareIds(models.Model):
    name = models.CharField(max_length=32 , default = "None", blank=False, primary_key=True)
    symbol = models.CharField(max_length=MAX_LENGTH_TICKER_SYMBOL, blank=True )
    wkn = models.CharField(max_length=MAX_LENGTH_WKN, default = "None", blank=True)
    isin = models.CharField(max_length=MAX_LENGTH_ISIN, default = "None", blank=True)
    isMainShare = models.BooleanField(default = False)

    def __str__(self):
        return self.name + ":" + self.symbol + "," + self.wkn + "," +self.isin
    
    class Meta:
        verbose_name = "Share/Stock IDs"
        verbose_name_plural = verbose_name


