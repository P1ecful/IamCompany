from django import template
from iamcompany_shop.models import Product, Category

register = template.Library()

@register.inclusion_tag('product_list.html')
def show_products():
    product = Product.objects.all()
    category = Category.objects.all()
    return {'product': product,
            'category': category}
