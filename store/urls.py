from django.urls import path,include
from . import views
from django.contrib.auth.models import User
from .models import *
app_name='store'
urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name="add_cart"),
    path('cartdetails',views.cart,name="cart"),
    path('cartr-emove/<int:product_id>/',views.cart_remove,name="cart_remove"),
    path('cart-delete/<int:product_id>/',views.cart_delete,name="cart_delete"),
]