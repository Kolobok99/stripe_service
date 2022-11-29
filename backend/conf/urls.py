from django.contrib import admin
from django.urls import path, include

from apps.api import urls as api_urls
from apps.orders import urls as orders_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
    path('', include(orders_urls))
]
