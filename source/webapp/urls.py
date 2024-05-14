from django.contrib import admin
from django.urls import path
from webapp.views import (IndexView, ProductView, ProductUpdateView, ProductDeleteView, ProductCreateView,
                          RoomProductsView, OrderCreateView,
                          BasketAddView, BasketDeleteOneView, BasketView, BasketDeleteView)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),

    path('rooms/<int:pk>/products/', RoomProductsView.as_view(), name='room_products'),
    path('basket/', BasketView.as_view(), name='basket_view'),
    path('product/<int:pk>/add-to-cart/', BasketAddView.as_view(), name='product_add_to_basket'),
    path('basket/<int:pk>/delete/', BasketDeleteView.as_view(), name='basket_delete'),
    path('basket/<int:pk>/delete-one/', BasketDeleteOneView.as_view(), name='basket_delete_one'),
    path('order/create/', OrderCreateView.as_view(), name='order_create')

]
