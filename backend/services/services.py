from typing import Union

import stripe

from apps.orders.models import Item, Order, Discount, Tax
from conf.settings import STRIPE_SECRET_API_KEY
from conf.settings import API_HOST

stripe.api_key = STRIPE_SECRET_API_KEY



def create_session(instance: Union[Item, Order]) -> dict:
    """
    Создает stripe.Session оплаты для instance
    :param
        instance: (Item/Order) - инстанс модели Item/Order
    :return:
        словарь созданной сессии
    """

    disc = []

    line_items = create_line_items(instance)

    if type(instance) is Order and instance.discount:
        discount_id = create_discount(instance.discount)['id']
        disc = [{'coupon': discount_id}]

    session: dict = stripe.checkout.Session.create(
        success_url=f"https://{API_HOST}/success",
        cancel_url=f"https://{API_HOST}/cancel",
        line_items=line_items,
        mode="payment",
        discounts=disc
    )
    return session


def create_line_items(instance: Union[Item, Order]) -> [dict]:
    """
    Генерирует список словарей item'ов, которые будут включены в stripe.Session
    :param
        instance: (Item/Order) - инстанс модели Item/Order
    :return:
        [item's]
    """

    items = []

    if type(instance) is Item:
        items = [
            {
                "price": f"{get_or_create_product_price(instance)}",
                "quantity": 1,
            }
        ]
    elif type(instance) is Order:
        items = [
            {
                'price': get_or_create_product_price(item),
                "quantity": 1,
            } for item in instance.items.all()
        ]
        if instance.tax:
            new_tax_id = create_tax(instance.tax)
            for item in items:
                item['tax_rates'] = [new_tax_id]
    return items


def get_or_create_product_price(item: Item):
    """Получает/Создает Price Item'a"""

    item_prices = stripe.Price.search(
        query=f"active:'true' AND product:'prod_{item.pk}'",
    )
    for price in item_prices:
        if price['unit_amount'] == item.price:
            return price['id']
    price = create_price(item)
    return price['id']


def create_price(item:Item) -> dict:
    """Создает Price для переданного item в Stripe'е"""

    price = stripe.Price.create(
        unit_amount=int(item.price * 100),
        currency=f"{item.currency}",
        product=f"prod_{item.pk}",
    )
    return price


def create_discount(discount: Discount):
    """Создает Coupon переданного discount в Stripe'е"""

    stripe_discount = stripe.Coupon.create(
        percent_off=discount.percentage,
        duration="once",
    )
    return stripe_discount


def create_product(item:Item) -> None:
    """Создает Product переданного item в Stripe'е"""

    stripe.Product.create(
        id=f"prod_{item.pk}",
        name=f"Item {item.pk}",
        description=item.description,
    )


def update_product(item:Item) -> None:
    """Обновляет Product переданного item в Stripe'е"""

    stripe.Product.modify(
        sid=f"prod_{item.pk}",
        name=f"Item {item.pk}",
        description=item.description,
    )


def create_tax(tax: Tax):
    """Создает TaxRate переданного tax в Stripe'е"""

    stripe_tax = stripe.TaxRate.create(
      display_name="VAT",
      description="VAT Russia",
      jurisdiction="RU",
      percentage=tax.percentage,
      inclusive=False,
    )
    return stripe_tax['id']