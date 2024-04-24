from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import View, TemplateView
from webapp.models import Product, Basket
from django.views.generic import FormView

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


class BasketOrderView(TemplateView):
    template_name = 'basket_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        for item in Basket.objects.all():
            total += item.product.price * item.amount

        context['basket'] = Basket.objects.all().distinct()
        context['total'] = total
        return context
