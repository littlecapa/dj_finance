from django.db import models
from .shares_models import shareIds

periodChoices = [("month", "Month"), ("month m.", "Month manually"), ("onetime", "Onetime"), ("planned", "Planned")]

class strategy(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    summary = models.TextField(blank=True)
    isActive  = models.BooleanField(default = True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "My Strategies"

class strategyShares(models.Model):
    strategy_name = models.ForeignKey('strategy', on_delete=models.CASCADE)
    shares_name = models.ForeignKey('shareIds', on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=periodChoices)
    invest = models.DecimalField(max_digits=10, decimal_places=2)
    numberShares = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    info = models.TextField(blank=True)

    def __str__(self):
        return str(self.strategy_name) + "->" + str(self.shares_name)

    class Meta:
        verbose_name_plural = "Shares for Strategy"
        unique_together = ('strategy_name', 'shares_name')

