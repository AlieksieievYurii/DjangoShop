from django.urls import path
from .views import base_view
from .views import product_view
from .views import category_view
from .views import cart_view
from .views import add_to_cart_view
from .views import remove_from_card_view

urlpatterns = [
    path('', base_view),
    path('category/<category_slug>/', category_view, name='category_view'),
    path('product/<product_slug>/', product_view, name='product_view'),
    path('cart/', cart_view, name='cart'),
    path('add_to_cart/', add_to_cart_view, name='add_to_cart'),
    path('remove_item_from_cart/', remove_from_card_view, name='remove_product')
]