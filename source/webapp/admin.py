from django.contrib import admin
from webapp.models import Category, Room
from django.utils.translation import gettext_lazy as _


# ParentCategoryFilter:
# Фильтр для выбора категорий на основе родительской категории.
# В lookups мы собираем уникальные имена родительских категорий.
class ParentCategoryFilter(admin.SimpleListFilter):
    title = _('Родительская категория')
    parameter_name = 'parent_category'

    def lookups(self, request, model_admin):
        # Получаем уникальные родительские категории
        categories = set(model_admin.model.objects.exclude(parent=None).values_list('parent__name', flat=True))
        return [(cat, cat) for cat in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(parent__name=self.value())


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'room', 'name', 'parent']
    list_display_links = ('pk', 'name')
    list_filter = ['room', ParentCategoryFilter]
    ordering = ('room', 'parent')
    search_fields = ('name',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Room, RoomAdmin)
