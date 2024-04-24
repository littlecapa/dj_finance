from django.db import models
from .shares_models import shareIds

class blogEntry(models.Model):
    headLine = models.CharField(max_length=96)
    source = models.CharField(max_length=96, blank=True)
    url = models.URLField()
    picture_url  = models.URLField(blank=True)
    referencedStocks = models.TextField(blank=True, verbose_name="References to Stocks:", help_text="Use this Colab https://colab.research.google.com/drive/1yhgrlksevpURUSeDHN9RnU-lqWELjeCi?usp=sharing")
    stocksProcessed = models.BooleanField(default=False, verbose_name="Stocks already processed:")
    summary = models.TextField(blank=True)
    plannedAction = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headLine
    
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"  # Optional, for plural form

class blog_shares(models.Model):
    blog_id = models.ForeignKey('blogEntry', on_delete=models.CASCADE)
    shares_name = models.ForeignKey('shareIds', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog_id) + "-->" + str(self.shares_name)
    
    class Meta:
        verbose_name = "In Blog referenced Stocks"
        verbose_name_plural = verbose_name
        unique_together = ('blog_id', 'shares_name')
