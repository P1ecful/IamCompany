from django.contrib import admin
from django.urls import path, include
from iamcompany_shop import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
