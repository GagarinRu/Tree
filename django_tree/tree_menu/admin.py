from django.contrib import admin
from django.contrib.auth.models import Group

from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'url')
    list_filter = ('menu_name',)
    search_fields = ('name', 'menu_name', 'url')
    fields = ('name', 'parent', 'menu_name', 'url')


admin.site.unregister(Group)
admin.site.empty_value_display = 'Не задано'
