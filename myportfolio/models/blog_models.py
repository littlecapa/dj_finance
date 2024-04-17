from django.db import models
from .shares_models import shareIds

class blogEntry(models.Model):
    headLine = models.CharField(max_length=96)
    source = models.CharField(max_length=96, blank=True)
    url = models.URLField()
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
    shares_id = models.ForeignKey('shareIds', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog_id) + "-->" + str(self.shares_id)
    
    class Meta:
        verbose_name = "In Blog referenced Stocks"
        verbose_name_plural = verbose_name
