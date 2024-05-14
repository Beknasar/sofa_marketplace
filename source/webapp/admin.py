from django.contrib import admin
from webapp.models import Category, Room, Product, Order, OrderProduct, Basket


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'room', 'name']
    list_display_links = ('pk', 'name')
    list_filter = ['room',]
    ordering = ('room',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'amount', 'price', 'room', 'category']
    list_display_links = ('pk', 'name')
    list_filter = ('room', 'category',)
    search_fields = ('name',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


class OrderProductAdmin(admin.TabularInline):
    model = OrderProduct
    fields = ('product', 'amount')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'phone', 'date_create']
    list_display_links = ('pk', 'name')
    inlines = (OrderProductAdmin,)
    ordering = ['-date_create']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Order, OrderAdmin)
