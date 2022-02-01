from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from shop.models import Category,Product
from .models import *

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart.save()

    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item=Cartitem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item=Cartitem.objects.create(product=product,cart=cart,quantity=1)
        cart_item.save()
    return redirect('store:cart')
def cart(request,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=Cartitem.objects.filter(cart=cart,active=True)

    except ObjectDoesNotExist:
        pass

    return render(request,"cart.html",{'cartitem':cart_items,'cart':cart})

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=Cartitem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        print("remove")
    else:
        cart_item.delete()
        print("delete")


    return redirect('store:cart')
def cart_delete(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=Cartitem.objects.get(product=product,cart=cart)
    cart_item.delete()
    print("delete")
    return redirect('store:cart')

