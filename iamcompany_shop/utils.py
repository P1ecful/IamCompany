from .models import *
from typing import Any, Dict


class DataMixin:
    model = Category
    extra_context = {"categories": Category.objects.all()}

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

class CategoryMixin:
    def get_context_data(self, *, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')
        context['category'] = Product.objects.filter(category__slug = category_slug)
        return context
    