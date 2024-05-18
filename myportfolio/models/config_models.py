from django.db import models

sourceChoices = [("comdirect", "Extract Comdirect Share Names, WKN and ISIN"), ("comdirect portfolio", "Extract Comdirect Portfolio"), ("es", "Effektenspiegel"), ("scalable", "Scalable")]

class upload(models.Model):
    uploadData = models.CharField(max_length=32, choices=sourceChoices, primary_key=True)
    info = models.TextField(blank=True)

class attrNames(models.Model):
    source = models.CharField(max_length=32, choices=sourceChoices, primary_key=True)
    attrName = models.CharField(max_length=32)
    attrIsin = models.CharField(max_length=32)
    attrWkn = models.CharField(max_length=32)
    attrCurrency = models.CharField(max_length=32)
    attrEtf = models.CharField(max_length=32)
    attrValue = models.CharField(max_length=32)
    attrNumber = models.CharField(max_length=32)
    attrDatum = models.CharField(max_length=32, default = "")

    def __str__(self):
        return self.source
    
    class Meta:
        verbose_name = "Config: Attribut Names for Stock Infos"
        verbose_name_plural = verbose_name


