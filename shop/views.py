from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)

class PurchaseCreate(CreateView):
    model = Purchase  
    fields = ['product', 'person', 'address']  

    def form_valid(self, form):
        self.object = form.save()

def purchase_form(request):
    quantities = {}  # для хранения количества товаров
    price = 0  # Общая стоимость товаров без скидки
    total_price = 0  # Итоговая стоимость с учетом скидки
    items = []  # Список покупок
    discount = 0  # Сумма скидки

    # Обработка данных из POST-запроса
    for key, value in request.POST.items():
        # Проверка, если ключ соответствует количеству товара
        if key.startswith('quantity_') and value:
            product_id = int(key.split('_')[1])  # Извлечение ID товара из ключа
            quantity = int(value)  # Извлечение количества товара
            product = Product.objects.get(pk=product_id)  # Получение товара по ID

            # Подсчет стоимости текущего товара
            total_item_price = product.price * quantity
            price += total_item_price

            # Добавление данных о товаре в список покупок
            items.append({
                'product': product,
                'quantity': quantity,
                'total_item_price': total_item_price,
            })

        # Если в корзине более одного товара, применяем скидку
        if len(items) > 1:
            discount = 0.1 * price  
            total_price = 0.9 * price 
        else:
            total_price = price  

    context = {
        'items': items,  
        'price': price,  
        'total_price': total_price,  
        'discount': discount,  
    }

    return render(request, 'shop/purchase_form.html', context)

def finalize_purchase(request):
    name = request.POST.get('name', 'Уважаемый клиент')
    address = request.POST.get('address', 'Адрес не указан')

    context = {
        'name': name,  # Имя клиента
        'address': address,  # Адрес доставки
    }

    print(context)

    return render(request, 'shop/finalize_purchase.html', context)
