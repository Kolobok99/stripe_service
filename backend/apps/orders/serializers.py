
from rest_framework import serializers

from apps.orders.models import Order, Item, Discount, Tax
from apps.orders.validators import OrderCurrencyValidator
from services.services import create_product, update_product


class OrderSerializer(serializers.ModelSerializer):
    """Сериалазйер модели Order"""

    class Meta:
        model = Order
        fields = "__all__"
        validators = [OrderCurrencyValidator]


class TaxSerializer(serializers.ModelSerializer):
    """Сериалазйер модели Tax"""

    class Meta:
        model = Tax
        fields = "__all__"


class DiscountSerializer(serializers.ModelSerializer):
    """Сериалазйер модели Discount"""

    class Meta:
        model = Discount
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Item"""

    def create(self, validated_data):
        instance = super(ItemSerializer, self).create(validated_data)
        create_product(instance)
        return instance

    def update(self, instance, validated_data):
        instance = super(ItemSerializer, self).update(instance, validated_data)
        update_product(instance)
        return instance

    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'price',
            'currency',
            'description',
        ]
