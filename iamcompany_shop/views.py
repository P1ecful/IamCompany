from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Category, Product
from .utils import *

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer


# Страницы сайта
class MainPage(DataMixin, ListView): template_name = 'index.html'
class FaqPage(DataMixin, ListView): template_name = 'Faq.html'
class DeveloperPage(DataMixin, ListView): template_name = 'about_developer.html'
class CategoryPage(DataMixin, CategoryMixin, ListView): template_name = 'catalog.html'

def ProductPage(requests, product_slug, category_slug):
    #FIXME
    category = Product.objects.filter(category__slug = category_slug)
    detail = Product.objects.get(slug = product_slug)
    return render(requests, 'product_card.html', context = {'title': detail.title})

# Api 
class CatalogAPIView(APIView):
    def get(self, response):
        catalog_items = Product.objects.all()
        return Response({'items': ProductSerializer(catalog_items, many=True).data})
    