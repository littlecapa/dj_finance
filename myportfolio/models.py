from django.db import models

# Create your models here.

MAX_LENGTH_TICKER_SYMBOL = 12

class MainShares(models.Model):
    name = models.CharField(max_length=32 , default = "None")
    symbol = models.CharField(max_length=MAX_LENGTH_TICKER_SYMBOL )

    def __str__(self):
        return self.symbol
    
    class Meta:
        verbose_name = "Main Shares"
        verbose_name_plural = "Main Shares"  # Optional, for plural form

class Category(models.Model):
    name = models.CharField(max_length=32)
    priority = models.IntegerField()

    class Meta:
        verbose_name = "Link Category"
        verbose_name_plural = "Categories"  # Optional, for plural form

    def __str__(self):
        return self.name

class Link(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    url = models.URLField()

    def __str__(self):
        return self.name

class SearchHistory(models.Model):

    symbol = models.CharField(max_length=MAX_LENGTH_TICKER_SYMBOL )
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
