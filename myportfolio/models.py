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