from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.base import View
from webapp.models import Product, Basket, Order, OrderProduct
from django.views.generic import FormView
from webapp.forms import OrderForm
from django.db import transaction


class BasketDeleteView(View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        product_from_basket = Basket.objects.get(product_id=pk)
        product_from_basket.delete()
        return redirect('webapp:basket_view')


class BasketCountView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)

        try:
            basket_product = Basket.objects.get(product__pk=product.pk)
        except Basket.DoesNotExist:
            basket_product = None
        if basket_product:
            if basket_product.amount <= product.amount:
                basket_product.amount += 1
            basket_product.save()
        elif basket_product is None:
            if product.amount > 0:
                basket_product = Basket.objects.create(
                    product=product,
                    amount=1
                )
                basket_product.save()

        return redirect('webapp:index')


class BasketOrderView(FormView):
    template_name = 'basket_view.html'
    form_class = OrderForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_total = []
        total = 0
        for item in Basket.objects.all():
            total += item.product.price * item.amount

        context['basket'] = Basket.objects.all()
        context['total'] = total
        context['form'] = OrderForm
        return context

    @transaction.atomic
    def form_valid(self, form):
        self.order = form.save()
        basket_items = Basket.objects.all()
        for item in basket_items:
            product = item.product

            # Проверяем, нужно ли изготавливать товар на заказ
            if product.status == "for order":
                # Если товар есть на складе, уменьшаем его количество
                if product.amount > 0:
                    available_to_deduct = min(product.amount, item.amount)
                    product.amount -= available_to_deduct
                    product.save()
                # Вне зависимости от наличия добавляем весь запрашиваемый товар в заказ
                OrderProduct.objects.create(
                    amount=item.amount,
                    order=self.order,
                    product=product
                )
            # Для товаров не на заказ проверяем наличие и списываем необходимое количество
            else:
                if product.amount >= item.amount:
                    product.amount -= item.amount
                    product.save()
                    OrderProduct.objects.create(
                        amount=item.amount,
                        order=self.order,
                        product=product
                    )
                else:
                    # Обработка случая, когда товара недостаточно на складе
                    form.add_error(None, 'Недостаточно товара на складе для продукта {}'.format(product.name))
                    return self.form_invalid(form)

        basket_items.delete()  # Удаление всех элементов корзины после обработки
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:index')
