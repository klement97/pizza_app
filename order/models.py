from django.db import models


class PizzaSize(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.description} ${self.price}'


class PizzaTopping(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.description} ${self.price}'


class Pizza(models.Model):
    toppings = models.ManyToManyField(PizzaTopping)


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    extra_toppings = models.ManyToManyField(PizzaTopping)
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE, related_name='pizzas')
