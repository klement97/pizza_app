from decimal import Decimal

import requests
from django.conf import settings
from django.db import models

from order.utils import ORDER_STATUS_CHOICES, prepare_receipt_data


class Size(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.description} ${self.price}'


class Topping(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.description} ${self.price}'


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    toppings = models.ManyToManyField(Topping, related_name='pizzas')

    @property
    def total_price(self) -> Decimal:
        """
        Total price is sum of all topping prices.
        """
        price = Decimal(0)
        for topping in self.toppings.all():
            price += topping.price

        return price

    def __str__(self):
        return f'{self.name} -- ${self.total_price}'


class Order(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    notes = models.TextField(blank=True)
    address = models.CharField(max_length=254)
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES)

    @property
    def total_price(self) -> Decimal:
        """
        Total price is sum of pizza prices in this order.
        """
        price = Decimal(0)
        for pizza in self.pizzas.all():
            price += pizza.total_price

        return price

    def send_to_delivery(self):
        pass

    def mark_as_delivered(self):
        pass

    def print_receipt(self):
        requests.post(
            url=settings.RECEIPT_MICROSERVICE,
            data=prepare_receipt_data(order=self)
        )

    def save(self, *args, **kwargs):
        self.price = self.total_price
        self.print_receipt()
        super().save(*args, **kwargs)


class PizzaOrder(models.Model):
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        related_name='pizza_orders'
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name='pizza_orders'
    )
    extra_toppings = models.ManyToManyField(
        Topping,
        related_name='pizza_orders'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='pizzas'
    )

    def __str__(self):
        return f'{self.pizza.name} -- {self.size.description}'

    @property
    def total_price(self) -> Decimal:
        """
        Total price is sum of the following:
            - Pizza total price
            - Size price
            - Sum of toppings
        """
        price = self.pizza.total_price + self.size.price
        for topping in self.extra_toppings.all():
            price += topping.price

        return price
