from typing import Dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
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


def add_to_cart_view(request, product_slug):
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
    product = Product.objects.get(slug=product_slug)
    new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.save()
        return HttpResponseRedirect('/cart/')


def remove_from_card_view(request, product_slug):
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
    product = Product.objects.get(slug=product_slug)
    cart.items.get(product=product).delete()
    cart.save()
    return HttpResponseRedirect('/cart/')

