from django.db import models

# Моделька Постовщика
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
# Моделька Контракта
class Contract(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    contract_start = models.DateField()
    contract_end = models.DateField()
    terms = models.TextField()

    def __str__(self):
        return f"{self.supplier.name} ({self.contract_start} - {self.contract_end})"
# Моделька Заказа
class Order(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField()
    delivery_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order to {self.supplier.name} on {self.order_date}"
