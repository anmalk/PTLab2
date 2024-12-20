from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/<int:product_id>/', views.PurchaseCreate.as_view(), name='buy'),
    path('purchase_form/', views.purchase_form, name='purchase_form'),
    path('finalize_purchase/', views.finalize_purchase, name='finalize_purchase'),

]

