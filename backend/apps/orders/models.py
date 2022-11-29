from django.db import models


class Item(models.Model):
    """Модель Предмета, добавляемого в Заказ (Order)"""

    currency_choices = (
        ('usd', 'Доллар'),
        ('rub', 'Рубль')
    )

    name = models.CharField("Имя", max_length=16)
    description = models.TextField("Описание")
    price = models.FloatField("Цена")
    currency = models.CharField("Валюта", choices=currency_choices, max_length=3)

    def __str__(self):
        return f"{self.pk} {self.name} {self.currency} {self.price}"


class Order(models.Model):
    """Модель заказа"""

    items = models.ManyToManyField("Item")
    discount = models.ForeignKey("Discount", on_delete=models.SET_NULL, null=True)
    tax = models.ForeignKey("Tax", on_delete=models.SET_NULL, null=True)


class Discount(models.Model):
    """Модель скидки Заказа (Order)"""

    percentage = models.FloatField("Процент скидки")


class Tax(models.Model):
    """Модель налоговой ставки"""

    percentage = models.FloatField("Налоговая ставка")
