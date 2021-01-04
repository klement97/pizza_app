ORDER_STATUS_CHOICES = [
    (0, 'new'),
    (1, 'delivery_sent'),
    (2, 'delivered')
]


def prepare_receipt_data(order):
    from order.serializers import OrderSerializer
    return OrderSerializer(instance=order).data
