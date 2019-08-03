from typing import Dict

from django.shortcuts import render
from .models import Category
from .models import Product


def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all_available()
    context: Dict[str, any] = {
        'categories': categories,
        'products': products
    }
    return render(request, 'base.html', context=context)


def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context: Dict[str, any] = {
        'product': product
    }
    return render(request, 'product.html', context=context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    context: Dict[str, any] = {
        'category': category
    }
    return render(request, 'category.html', context=context)
