from django.contrib import admin
from django.urls import path
from .views import IndexView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
