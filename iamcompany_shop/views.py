from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Product
from .utils import *

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer


# Страницы сайта
class MainPage(DataMixin, ListView): template_name = 'index.html'
class FaqPage(DataMixin, ListView): template_name = 'Faq.html'
class DeveloperPage(DataMixin, ListView): template_name = 'about_developer.html'
  
def shop_products(request, category_slug):
    return render(request, 'catalog.html', {"category": Product.objects.filter(category__slug = category_slug),
                                            "categories": Category.objects.all()})

# Api 
class CatalogAPIView(APIView):
    def get(self, response):
        catalog_items = Product.objects.all()
        return Response({'items': ProductSerializer(catalog_items, many=True).data})
    