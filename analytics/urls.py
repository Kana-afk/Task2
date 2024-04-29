
from django.urls import path
from .views import total_orders_by_supplier, average_order_cost_by_supplier, detailed_supplier_analysis

urlpatterns = [
    path('total-orders/', total_orders_by_supplier, name='total_orders_by_supplier'),
    path('average-order-cost/', average_order_cost_by_supplier, name='average_order_cost_by_supplier'),
    path('detailed-analysis/', detailed_supplier_analysis, name='detailed_supplier_analysis'),
]
