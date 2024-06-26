from django.contrib import admin
from webapp.models import Category, Room, Product, Order, OrderProduct, Delivery


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


class DeliveryAdmin(admin.ModelAdmin):
    model = Delivery
    list_display = ('__str__', 'delivery_date', 'status')
    readonly_fields = ['order']
    list_display_links = ('__str__',)


class DeliveryInline(admin.StackedInline):
    model = Delivery
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'phone', 'date_create', 'related_model_field']
    list_display_links = ('pk', 'name')
    inlines = (OrderProductAdmin, DeliveryInline)
    ordering = ['-date_create']
    readonly_fields = ['user']
    search_fields = ['name', 'phone']
    list_filter = ['date_create']
    actions = ['export_to_csv', 'cancel_order']

    def related_model_field(self, order_obj):
        return order_obj.delivery.get_status_display()
    related_model_field.short_description = 'Статус'

    def cancel_order(self, request, queryset):
        for order in queryset:
            if order.delivery.status != 'cancelled':
                order.delivery.status = 'cancelled'
                order.delivery.save()
                # Возвращаем товары на склад
                for order_product in order.order_products.all():
                    product = order_product.product
                    product.amount += order_product.amount
                    product.save()
        self.message_user(request, "Выбранные заказы были отменены и товары были возвращены на склад")

    cancel_order.short_description = "Отменить выбранные заказы и вернуть товары"

    def export_to_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'Name', 'Phone', 'Date Created', 'Status'])

        for order in queryset:
            writer.writerow([order.pk, order.name, order.phone, order.date_create, order.delivery.status])

        return response

    export_to_csv.short_description = "Export to CSV"


admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Order, OrderAdmin)
