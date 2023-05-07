from django.contrib import admin
from django.utils.html import mark_safe
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_display = ('category', 'title', 'size')
     list_filter = ('category', 'size')
     fieldsets = (
        ('Представление продукта', {'fields': ('title','product_photo', 'cost', 'category', 'slug')}),
        ('Характеристики', {'fields': ('size', 'weight')}),
     )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ("name", )}


