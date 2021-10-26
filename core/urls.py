from django.urls import path
from .views import (
    CheckoutView,
    ItemDetailView,
    HomeView,
    Products_Home,
    Products_ByCat,
    Products_AllDesc,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    Landing,
    show_Categories
)

app_name = 'core'

urlpatterns = [
    path('', Landing, name='home'),
    path('products/', Products_Home, name='products'),
    path('products_bycat/<cat_id>/', Products_ByCat, name='prod_Cat'),
    path('products_alldesc/<cat_id>/', Products_AllDesc, name='prod_Desc'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView, name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
