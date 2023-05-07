from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view()),
    path("FAQ/", FaqPage.as_view()),
    path('o-razrabotchike/', DeveloperPage.as_view()),
    path('catalog/<slug:category_slug>/', shop_products),
]
