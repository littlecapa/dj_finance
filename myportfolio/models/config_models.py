from django.db import models

sourceChoices = [("comdirect", "Comdirect"), ("es", "Effektenspiegel"), ("scalable", "Scalable")]

class attrNames(models.Model):
    source = models.CharField(max_length=32, choices=sourceChoices, primary_key=True)
    attrName = models.CharField(max_length=32)
    attrIsin = models.CharField(max_length=32)
    attrWkn = models.CharField(max_length=32)
    attrCurrency = models.CharField(max_length=32)
    attrEtf = models.CharField(max_length=32)

    def __str__(self):
        return self.source
    
    class Meta:
        verbose_name = "Config: Attribut Names for Stock Infos"
        verbose_name_plural = verbose_name


