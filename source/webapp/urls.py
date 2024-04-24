from django.contrib import admin
from django.urls import path
from .views import (IndexView, ProductView, ProductUpdateView, ProductDeleteView, ProductCreateView,
                    RoomProductsView, BasketView, BasketCountView, BasketDeleteView)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),

    path('rooms/<int:pk>/products/', RoomProductsView.as_view(), name='room_products'),
    path('basket/product/<int:pk>/', BasketCountView.as_view(), name='basket_count'),
    path('basket/', BasketView.as_view(), name='basket_view'),
    path('basket/<int:pk>/', BasketDeleteView.as_view(), name='basket_delete')
]
