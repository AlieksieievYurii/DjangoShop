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