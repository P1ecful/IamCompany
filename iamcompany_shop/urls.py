from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view()),
    path('catalog/<slug:category_slug>/', shop_products),

    path("FAQ/", faq),
]
