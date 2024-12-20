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
    # Предположим, что информация о выбранных товарах передается в POST запросе
    selected_products = request.POST.getlist('products')  # Список ID товаров
    quantities = request.POST.getlist('quantities')  # Список количеств для каждого товара

    items = []
    total_price = 0

    # Находим товары в базе данных и подсчитываем стоимость
    for product_id, quantity in zip(selected_products, quantities):
        product = Product.objects.get(pk=product_id)
        quantity = int(quantity)  # Убедимся, что это число
        total_item_price = product.price * quantity
        total_price += total_item_price
        items.append({
            'product': product,
            'quantity': quantity,
            'total_item_price': total_item_price,
        })

    context = {
        'items': items,
        'total_price': total_price,
    }

    return render(request, 'shop/purchase_form.html', context)