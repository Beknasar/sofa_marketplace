from django.contrib import admin
from django.urls import path
from .views import IndexView, ProductView, ProductUpdateView, ProductDeleteView, ProductCreateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/create/', ProductCreateView.as_view(), name='product_create')
]
