from django.contrib import admin
from .models import Category
from .models import Brand
from .models import Product
from .models import CartItem
from .models import Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
