from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.core.paginator import Paginator

from .models import Category, Product, Banner
from .utils import DataMixin, CategoryMixin
from .serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from typing import Any, Dict


# Страницы сайта

class FaqPage(DataMixin, ListView): template_name = 'Faq.html'
class DeveloperPage(DataMixin, ListView): template_name = 'about_developer.html'
class CategoryPage(DataMixin, CategoryMixin, ListView): template_name = 'catalog.html'

class MainPage(DataMixin, ListView): 
    template_name = 'main.html'

    def get_context_data(self, *, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        return context
    
def ProductPage(requests, product_slug, category_slug):
    category = Product.objects.filter(category__slug = category_slug)
    detail = Product.objects.get(slug = product_slug)
    return render(requests, 'product_card.html', context = {'title': detail.title,
                                                            'photo': detail.product_photo})

# Api 
class CatalogAPIView(APIView):
    def get(self, response):
        catalog_items = Product.objects.all()
        return Response({'items': ProductSerializer(catalog_items, many=True).data})
    