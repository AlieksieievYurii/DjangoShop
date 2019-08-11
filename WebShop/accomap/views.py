from decimal import Decimal
from typing import Dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse

from .models import Category
from .models import Product
from .models import Cart
from .models import CartItem


def base_view(request):
    try:
        cart_id: int = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    products = Product.objects.all_available()
    context: Dict[str, any] = {
        'categories': categories,
        'products': products,
        'cart': cart
    }
    return render(request, 'base.html', context=context)


def product_view(request, product_slug):
    cart = Cart.objects.first()
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    context: Dict[str, any] = {
        'product': product,
        'categories': categories,
        'cart': cart
    }
    return render(request, 'product.html', context=context)


def category_view(request, category_slug):
    try:
        cart_id: int = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products_of_category = category.product_set.all()
    context: Dict[str, any] = {
        'categories': categories,
        'category': category,
        'products_of_category': products_of_category,
        'cart': cart
    }
    return render(request, 'category.html', context=context)


def cart_view(request):
    try:
        cart_id: int = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context: Dict[str, any] = {
        'cart': cart
    }
    return render(request, 'cart.html', context=context)


def add_to_cart_view(request):
    try:
        cart_id: int = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product_slug = request.GET.get('product_slug')
    cart.add_to_cart(product_slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse({'cart_total': cart.items.count(), 'cart_total_price': cart.cart_total})


def remove_from_card_view(request):
    try:
        cart_id: int = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)

    cart.remove_from_cart(request.GET.get('product_slug'))
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse({'cart_total': cart.items.count(), 'cart_total_price': cart.cart_total})


def change_item_qty(request):
    try:
        cart_id: int = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    qty = request.GET.get('qty')
    item_id = request.GET.get('item_id')
    cart_item = CartItem.objects.get(id=int(item_id))
    cart_item.qty = int(qty)
    cart_item.item_total = int(qty) * Decimal(cart_item.product.price)
    cart_item.save()
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse({
        'cart_total': cart.items.count(),
        'item_total': cart_item.item_total,
        'cart_total_price': cart.cart_total
    })
