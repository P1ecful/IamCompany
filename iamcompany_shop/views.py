from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout

from .models import Category, Product
from .utils import DataMixin, CategoryMixin
from .serializers import ProductSerializer
from .forms import LoginUserForm, RegisterUserForm

from rest_framework.response import Response
from rest_framework.views import APIView

from typing import Any, Dict


# Страницы сайта
class MainPage(DataMixin, ListView): template_name = 'index.html'
class FaqPage(DataMixin, ListView): template_name = 'Faq.html'
class DeveloperPage(DataMixin, ListView): template_name = 'about_developer.html'
class CategoryPage(DataMixin, CategoryMixin, ListView): template_name = 'catalog.html'

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('main')



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
    