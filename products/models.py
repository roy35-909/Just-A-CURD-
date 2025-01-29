from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    product = models.CharField(max_length=255)

    def __str__(self):
        return self.name