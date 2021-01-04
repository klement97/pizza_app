from decimal import Decimal

import pytest
import requests

from order.test_utils import create_pizza, create_order, MockResponse


@pytest.mark.django_db
@pytest.mark.parametrize('number_of_toppings', list(range(0, 10)))
def test_pizza_price(number_of_toppings):
    # Preparation phase
    pizza = create_pizza(number_of_toppings=number_of_toppings)

    # Calculating results
    actual_price = pizza.total_price
    expected_price = Decimal(sum([t.price for t in pizza.toppings.all()]))

    # Assertion
    assert actual_price == expected_price


@pytest.mark.django_db
def test_order_save(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'post', mock_post)
    breakpoint()
    order = create_order()

    assert order.price is not None
