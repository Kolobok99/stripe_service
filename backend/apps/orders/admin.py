from django.contrib import admin

from apps.orders import models

list_of_models = [models.Item, models.Order, models.Tax, models.Discount]

for m in list_of_models:
    admin.site.register(m)

# strong_root_password