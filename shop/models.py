from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# модель для описания покупки
class Purchase(models.Model):
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        # представление объекта в виде строки
        return f"Заказ от {self.person} на {self.date}"

# модель для описания позиции в покупке (товар + количество)
class PurchaseItem(models.Model):
    # связь с покупкой 
    purchase = models.ForeignKey(Purchase, related_name="items", on_delete=models.CASCADE)
    # связь с товаром 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # количество товара
    quantity = models.PositiveIntegerField()

    # метод для расчета стоимости текущей позиции
    def total_price(self):
        # Цена товара умноженная на количество
        return self.product.price * self.quantity

    def __str__(self):
        # Представление объекта в виде строки
        return f"{self.quantity} x {self.product.name}"
