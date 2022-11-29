from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'item', views.ItemAPIViewSet, basename='item')
router.register(r'order', views.OrderAPIViewSet, basename='order')
router.register(r'discount', views.DiscountAPIViewSet, basename='discount')
router.register(r'tax', views.TaxAPIViewSet, basename='discount')


urlpatterns = router.urls

urlpatterns += [
    path('buy/item/<int:pk>/', views.BuyItemAPI.as_view(), name='buy_item'),
    path('buy/order/<int:pk>/', views.BuyOrderAPI.as_view(), name='buy_item'),
]
