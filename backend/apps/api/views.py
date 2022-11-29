from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from apps.orders.models import Order, Item, Discount, Tax
from apps.orders.serializers import OrderSerializer, ItemSerializer, DiscountSerializer, TaxSerializer
from services.services import create_session


class OrderAPIViewSet(viewsets.ModelViewSet):
    """APIViewSet модели Order"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DiscountAPIViewSet(viewsets.ModelViewSet):
    """APIViewSet модели Discount"""

    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class ItemAPIViewSet(viewsets.ModelViewSet):
    """APIView модели Item"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class TaxAPIViewSet(viewsets.ModelViewSet):
    """APIView модели Tax"""

    queryset = Tax.objects.all()
    serializer_class = TaxSerializer


class BuyItemAPI(RetrieveAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        session_id = create_session(instance)['id']
        return Response(
            {'session_id': session_id}
        )


class BuyOrderAPI(RetrieveAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        session_id = create_session(instance)['id']
        return Response(
            {'session_id': session_id}
        )

