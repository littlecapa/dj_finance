from django.db import models

# Create your models here.

class MainShares(models.Model):
    name = models.CharField(max_length=12, default = "None")
    symbol = models.CharField(max_length=12)

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