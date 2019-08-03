from django.urls import path
from .views import base_view
from .views import product_view
from .views import category_view

urlpatterns = [
    path('index/', base_view),
    path('category/<str:category_slug>/', category_view),
    path('product/<str:product_slug>/', product_view)
]