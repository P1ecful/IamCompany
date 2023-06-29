from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', cache_page(60 * 15)(MainPage.as_view()), name = 'main'),
    path("FAQ/", cache_page(60 * 15)(FaqPage.as_view()), name = 'faq'),
    path('o-razrabotchike/', cache_page(60 * 15)(DeveloperPage.as_view()), name = 'developer'),
    path('catalog/<slug:category_slug>/', CategoryPage.as_view(), name = 'catalog'),
    path('catalog/<slug:category_slug>/<slug:product_slug>/', ProductPage, name = 'product'),
    path('api/catalog/', CatalogAPIView.as_view(), name = "api_catalog"),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]

