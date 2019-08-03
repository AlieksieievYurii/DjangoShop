from django.urls import path
from .views import base_view

urlpatterns = [
    path('index/', base_view)
]