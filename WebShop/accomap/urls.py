from django.urls import path
from .views import base_view
from .views import product_view
from .views import category_view

urlpatterns = [
    path('', base_view),
    path('category/<category_slug>/', category_view, name='category_view'),
    path('product/<product_slug>/', product_view, name='product_view')
]