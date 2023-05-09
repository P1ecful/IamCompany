from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name = 'Main'),
    path("FAQ/", FaqPage.as_view(), name = 'FAQ'),
    path("korzina/", BasketPage.as_view(), name = "backet"),
    path('o-razrabotchike/', DeveloperPage.as_view(), name = 'developer'),
    path('catalog/<slug:category_slug>/', shop_products, name = 'catalog'),
]
