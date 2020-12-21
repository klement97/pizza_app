from django.db import models


class PizzaSize(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class PizzaTopping(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Pizza(models.Model):
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE, related_name='pizzas')
    toppings = models.ManyToManyField(PizzaTopping, related_name='pizzas')


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza)
