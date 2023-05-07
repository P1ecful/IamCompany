from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ("title",)}
     list_display = ('title', 'category')
     list_filter = ('category')

class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ("name", )}

admin.site.register(Product)
admin.site.register(Category)


