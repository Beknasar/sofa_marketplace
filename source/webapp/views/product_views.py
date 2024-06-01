from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from webapp.forms import SearchForm, ProductForm
from webapp.models import Product, Room
from .base_views import SearchView


class ContactView(TemplateView):
    template_name = 'contact.html'


class IndexView(SearchView):
    model = Product
    template_name = 'products/index.html'
    ordering = ['-room', 'name']
    search_fields = ['name__icontains']
    paginate_by = 8
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        rooms = Room.objects.all()
        context['rooms'] = rooms
        return context

    def get_queryset(self):
        return super().get_queryset().filter(amount__gt=0)


class ProductView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)

        context['product'] = product
        context['related_products'] = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]
        return context

    def get_queryset(self):
        return super().get_queryset().filter(amount__gt=0)


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'products/product_update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    permission_required = 'products.change_product'

    def get_queryset(self):
        return super().get_queryset().filter(amount__gt=0)

    def has_permission(self):
        return super().has_permission()

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'

    def has_permission(self):
        return super().has_permission()

    def get_queryset(self):
        return super().get_queryset().filter(amount__gt=0)


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductForm
    model = Product
    permission_required = 'webapp.add_product'

    def has_permission(self):
        return super().has_permission()

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class RoomProductsView(ListView):
    template_name = 'products/room_product.html'
    context_object_name = 'products'
    paginate_by = 8
    paginate_orphans = 0
    ordering = ['-category']

    def get_queryset(self):
        room_id = self.kwargs.get('pk')
        category_id = self.request.GET.get('category_id')

        if category_id:
            return Product.objects.filter(category__id=category_id, amount__gt=0)
        else:
            return Product.objects.filter(category__room__id=room_id, amount__gt=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        room = Room.objects.get(pk=pk)
        context['room'] = room
        context['categories'] = room.categories.all()
        return context



