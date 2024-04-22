from django.contrib import admin
from django.urls import path
from .views import IndexView, ProductView, ProductUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update')
]
