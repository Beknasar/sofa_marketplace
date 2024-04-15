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
#
# # SubCategoryFilter:
# # Фильтр для подкатегорий, который отображает только те подкатегории,
# # которые соответствуют выбранной родительской категории.
# # Это достигается путем проверки текущего значения parent_category в URL-параметрах.
# class SubCategoryFilter(admin.SimpleListFilter):
#     title = _('Подкатегория')
#     parameter_name = 'subcategory'
#
#     def lookups(self, request, model_admin):
#         parent_name = request.GET.get('parent_category')
#         if parent_name:
#             subcategories = set(model_admin.model.objects.filter(parent__name=parent_name).values_list('name', flat=True))
#             return [(sub, sub) for sub in subcategories]
#         return []
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(name=self.value())
#

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
