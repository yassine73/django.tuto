from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, default='Default variable', verbose_name='change the displayed name on ui')
    content = models.TextField(
        null = True, # variable will be null if not filled
        blank = True, # variable will be not required
        verbose_name = 'Description'
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, default=10.0)
    image = models.ImageField(upload_to="photos-%y-%m-%d", default='photos-26-09-02/IG-LOGO.png')
    active = models.BooleanField(default=True)
    category = models.CharField(
        max_length=50,
        blank=True,
        choices=[
            ('computer', 'computer'), # (name shown on ui, name shown on database)
            ('phone', 'phone'),
        ],
    )

    def __str__(self):
        return self.name

    class Meta:
        # verbose_name = 'test' # change the name in admin panel
        ordering = ['price'] # ordering by price, to desc order use -price


class Test(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    datetime = models.DateTimeField(default=datetime.now)