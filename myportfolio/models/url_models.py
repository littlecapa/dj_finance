from django.db import models

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