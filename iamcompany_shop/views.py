from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category, Product
from .utils import *

class MainPage(DataMixin, ListView): template_name = 'index.html'
class FaqPage(DataMixin, ListView): template_name = 'Faq.html'
class DeveloperPage(DataMixin, ListView): template_name = 'about_developer.html'
  
def shop_products(request, category_slug):
    return render(request, 'catalog.html', {"category": Product.objects.filter(category__slug = category_slug),
                                            "categories": Category.objects.all()})

