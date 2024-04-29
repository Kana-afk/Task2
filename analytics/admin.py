from django.contrib import admin
from .models import Supplier, Order, Contract

admin.site.register(Supplier)
admin.site.register(Contract)
admin.site.register(Order)

