from rest_framework import serializers

from apps.orders.models import Item


class OrderCurrencyValidator:
    """
    Валидтор OrderSerializer

    Проверяет, что order.items.all() имеют одну и ту же currency
    """

    requires_context = True

    def __init__(self, data, serializer):
        self.__call__(data, serializer)

    def __call__(self, data, serializer):

        instance_items = []

        if serializer.instance:
            instance_items = serializer.instance.items.all()
        data_items = data.get('items')

        items = instance_items + data_items
        currency = data_items[0].currency

        for item in items:
            if item.currency != currency:
                raise serializers.ValidationError('У позиций заказа разные валюты!')



