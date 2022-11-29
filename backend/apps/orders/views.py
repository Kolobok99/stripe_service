from django.views.generic import DetailView

from apps.orders.models import Order, Item
from conf.settings import STRIPE_PUBLISH_API_KEY, API_HOST


class BuyOrderPage(DetailView):
    """
    METHODS:
        GET:
            Возвращает HTML-файл с кнопкой, перенаправляющей на стр. оплаты Order
    """
    model = Order
    template_name = 'buy_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['host'] = API_HOST
        context['order'] = self.get_object()
        context['api_key'] = STRIPE_PUBLISH_API_KEY

        return context


class BuyItemPage(DetailView):
    """
    METHODS:
        GET: Возвращает HTML-файл с кнопкой, перенаправляющей на стр. оплаты Item
    """

    model = Item
    template_name = 'buy_item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['host'] = API_HOST
        context['item'] = self.get_object()
        context['api_key'] = STRIPE_PUBLISH_API_KEY

        return context