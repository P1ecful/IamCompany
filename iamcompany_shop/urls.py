from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name = 'main'),
    path("FAQ/", FaqPage.as_view(), name = 'faq'),
    path('o-razrabotchike/', DeveloperPage.as_view(), name = 'developer'),
    path('catalog/<slug:category_slug>/', CategoryPage.as_view(), name = 'catalog'),
    path('catalog/<slug:category_slug>/<slug:product_slug>/', ProductPage, name = 'product'),
    path('api/catalog/', CatalogAPIView.as_view(), name = "api_catalog"),
]

