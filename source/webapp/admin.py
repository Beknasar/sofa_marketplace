from django.contrib import admin
from webapp.models import Category, Room


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_filter = ['rooms']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Room, RoomAdmin)
