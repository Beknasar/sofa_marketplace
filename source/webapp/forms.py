from django import forms
from .models import Product, Order, Basket, Delivery


BROWSER_DATETIME_FORMAT = '%d.%m.%Y %H:%M'


class XDatepickerWidget(forms.TextInput):
    template_name = 'widgets/xdatepicker_widget.html'


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        exclude = ['order']


class OrderForm(forms.ModelForm):
    delivery_date = forms.DateTimeField(label='Дата доставки', required=False,
                                        input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
                                                       '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
                                                       '%Y-%m-%d %H:%M:%S'],
                                        widget=XDatepickerWidget)

    class Meta:
        model = Order
        fields = ['name', 'address', 'phone', 'comment', 'delivery_date']
        widgets = {'phone': forms.NumberInput}


class BasketAddForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['amount',]
