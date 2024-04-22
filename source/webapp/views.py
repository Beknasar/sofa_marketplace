from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from webapp.forms import SearchForm, ProductForm
from webapp.models import Product, Room, Category


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 8
    paginate_orphans = 0
    ordering = ['-room']

    def get_context_data(self, *, object_list=None, **kwargs):
        form = SearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            kwargs['search'] = search
        kwargs['form'] = form

        rooms = Room.objects.all()
        kwargs['rooms'] = rooms
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Product.objects.all()

        form = SearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(name__icontains=search) | Q(description__icontains=search))
        return data


class ProductView(DetailView):
    template_name = 'product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)

        context['product'] = product
        context['related_products'] = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]
        return context

    def get_queryset(self):
        return Product.objects.all()


class ProductUpdateView(UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    model = Product
    success_url = reverse_lazy('webapp:index')


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class RoomProductsView(ListView):
    template_name = 'room_product.html'
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

