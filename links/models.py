from django.db import models
from .utils import get_link_data

class Link(models.Model):
    name = models.CharField(max_length=255, blank=True)
    url = models.URLField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_difference = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        ordering = ['price_difference', '-created']

    def save(self, *args, **kwargs):
        name, price = get_link_data(self.url)
        old_price = self.current_price
        if self.current_price:
            if price != old_price:
                price_diff = price-old_price
                self.price_difference = price_diff
                self.old_price = old_price
        else:
            self.old_price = 0
            self.price_difference = 0
        self.name = name
        self.current_price = price
        super().save(*args, **kwargs)

    
    