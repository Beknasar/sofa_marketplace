from django.urls import path, include
from webapp.views import (IndexView,
                          ProductView,
                          ProductUpdateView,
                          ProductDeleteView,
                          ProductCreateView,
                          RoomProductsView,
                          OrderCreateView,
                          BasketAddView,
                          BasketDeleteOneView,
                          BasketView,
                          BasketDeleteView,
                          CancelDeliveryView)

app_name = 'webapp'

urlpatterns = [
    # ссылки на товары
    path('', IndexView.as_view(), name='index'),
    path('product/', include([
        path('<int:pk>/', include([
            path('', ProductView.as_view(), name='product_view'),
            path('update/', ProductUpdateView.as_view(), name='product_update'),
            path('delete/', ProductDeleteView.as_view(), name='product_delete'),
            path('add-to-basket/', BasketAddView.as_view(), name='product_add_to_basket'),
        ])),
        path('create/', ProductCreateView.as_view(), name='product_create'),
    ])),
    # ссылки на корзину
    path('basket/', include([
        path('', BasketView.as_view(), name='basket_view'),
        path('<int:pk>/', include([
            path('delete/', BasketDeleteView.as_view(), name='basket_delete'),
            path('delete-one/', BasketDeleteOneView.as_view(), name='basket_delete_one'),
        ])),
    ])),
    # ссылка на категорию товаров
    path('rooms/<int:pk>/products/', RoomProductsView.as_view(), name='room_products'),
    # ссылки на заказы
    path('order/', include([
        path('create/', OrderCreateView.as_view(), name='order_create'),
        path('<int:pk>/cancel_delivery/', CancelDeliveryView.as_view(), name='cancel_delivery')
    ])),
]
