from django.shortcuts import render
from django.db.models import Sum, Avg, Count
from .models import Supplier, Contract, Order
import pandas as pd

# Суммарная стоимость заказов по поставщикам
def total_orders_by_supplier(request):
    data = Order.objects.values('supplier__name').annotate(total_cost=Sum('total_cost')).order_by('-total_cost')
    return render(request, 'analytics/orders_summary.html', {'data': data})

# Средняя стоимость заказов по поставщикам
def average_order_cost_by_supplier(request):
    data = Order.objects.values('supplier__name').annotate(average_cost=Avg('total_cost')).order_by('-average_cost')
    return render(request, 'analytics/average_cost_summary.html', {'data': data})


# Использование Pandas для более сложного анализа
def detailed_supplier_analysis(request):
    query_set = Order.objects.all().values()
    df = pd.DataFrame(list(query_set))
    result = df.groupby('supplier_id')['total_cost'].agg(['sum', 'mean', 'count'])

    # Возвращаем DataFrame в HTML для отображения
    result_html = result.to_html()
    return render(request, 'analytics/detailed_analysis.html', {'result_html': result_html})
from django.shortcuts import render
from .models import Order

def total_orders_by_supplier(request):
    orders = Order.objects.all()
    return render(request, 'analytics/total_orders_by_supplier.html', {'orders': orders})





