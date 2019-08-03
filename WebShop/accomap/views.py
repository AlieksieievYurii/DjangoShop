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
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    context: Dict[str, any] = {
        'product': product,
        'categories': categories
    }
    return render(request, 'product.html', context=context)


def category_view(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products_of_category = category.product_set.all()
    context: Dict[str, any] = {
        'categories': categories,
        'category': category,
        'products_of_category': products_of_category
    }
    return render(request, 'category.html', context=context)
