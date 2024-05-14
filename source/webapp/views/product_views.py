from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from webapp.forms import SearchForm, ProductForm
from webapp.models import Product, Room
from .base_views import SearchView


class IndexView(SearchView):
    model = Product
    template_name = 'products/index.html'
    ordering = ['-room', 'name']
    search_fields = ['name_icontains']
    paginate_by = 8
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        rooms = Room.objects.all()
        context['rooms'] = rooms
        return context

    def get_queryset(self):
        return super().get_queryset()


class ProductView(DetailView):
    model = Product
    template_name = 'products/product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)

        context['product'] = product
        context['related_products'] = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]
        return context

    def get_queryset(self):
        return super().get_queryset()


class ProductUpdateView(UpdateView):
    template_name = 'products/product_update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    success_url = reverse_lazy('webapp:index')


class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductForm
    model = Product

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
            return Product.objects.filter(category__id=category_id)
        else:
            return Product.objects.filter(category__room__id=room_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        room = Room.objects.get(pk=pk)
        context['room'] = room
        context['categories'] = room.categories.all()
        return context



