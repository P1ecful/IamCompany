from .models import *

class DataMixin:
    model = Category
    extra_context = {"categories": Category.objects.all()}