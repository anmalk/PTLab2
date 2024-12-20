from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)



class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        # Сохраняем покупку в базе данных
        self.object = form.save()
        # Здесь можно обработать создание нескольких покупок для каждого товара
        return redirect('purchase_form')  # Перенаправление после успешной покупки
    
def purchase_form(request):
    quantities = {}
    price = 0
    total_price = 0
    items = []
    discount = 0
    # Получение данных из запроса
    for key, value in request.POST.items():
        if key.startswith('quantity_') and value:
            product_id = int(key.split('_')[1])  # Извлечение ID товара
            quantity = int(value)  # Количество
            product = Product.objects.get(pk=product_id)

            total_item_price = product.price * quantity
            price += total_item_price

            items.append({
                'product': product,
                'quantity': quantity,
                'total_item_price': total_item_price,
            })
        if len(items) > 1:
            discount = 0.1*price
            total_price = 0.9*price
        else: total_price = price

    
    context = {
        'items': items,
        'price': price,
        'total_price': total_price,
        'discount': discount,
    }

    return render(request, 'shop/purchase_form.html', context)