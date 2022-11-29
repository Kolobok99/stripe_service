from django.urls import path

from apps.orders.views import BuyItemPage, BuyOrderPage

urlpatterns = [
    path('item/<int:pk>/', BuyItemPage.as_view()),
    path('order/<int:pk>/', BuyOrderPage.as_view()),

]