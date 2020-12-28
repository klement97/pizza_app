from django.contrib import admin

from order import models

admin.site.register(models.Order)
admin.site.register(models.Pizza)
admin.site.register(models.PizzaOrder)
admin.site.register(models.Topping)
admin.site.register(models.Size)
