from django.urls import path
from .views import (
    item_list, products, HomeView, ItemDetailView, add_to_cart, remove_from_cart,OrderSummaryView, remove_single_item_from_cart,
    CheckOutView, PaymentView, AddCouponView, RequestRefundView
)
from . import views

app_name = 'core'

urlpatterns = [
    #path('', item_list, name='item-list'),
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('order-summary/',OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
]
