from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category, Product
from .utils import *

from django.http import HttpResponse

class MainPage(DataMixin, ListView): template_name = 'index.html'
  
def shop_products(request, category_slug):
    return render(request, 'catalog.html', {"category": Product.objects.filter(category__slug = category_slug),
                                            "categories": Category.objects.all()})


def faq(request):
    return HttpResponse("<h2> Страница FAQ </h2>")