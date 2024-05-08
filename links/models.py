from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=255, blank=True)
    url = models.URLField()
    current_price = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    price_difference = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        ordering = ['price_difference', '-created']

 
    
    