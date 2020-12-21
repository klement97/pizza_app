from django.contrib import admin

from order import models

admin.site.register(models.Order)
admin.site.register(models.Pizza)
admin.site.register(models.PizzaTopping)
admin.site.register(models.PizzaSize)
