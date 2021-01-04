from model_bakery import baker

from order.models import Pizza, Order


class MockResponse:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def create_pizza(number_of_toppings: int, **kwargs) -> Pizza:
    pizza = baker.make('order.Pizza', **kwargs)
    for _ in range(number_of_toppings):
        pizza.toppings.add(baker.make('order.Topping'))

    return pizza


def create_order() -> Order:
    order = baker.make('order.Order')
    baker.make('order.PizzaOrder', order=order)
    order.save()

    return order
