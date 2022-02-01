from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from store.models import Cartitem,Cart
from store.views import _cart_id
from shop.models import Product,Category



# Create your views here.
def check(request):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=Cartitem.objects.filter(cart=cart,active=True)

    except ObjectDoesNotExist:
        pass

    return render(request,"checkout.html",{'ct':cart_items,'c':cart})

def check_delete(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=Cartitem.objects.get(product=product,cart=cart)
    cart_item.delete()
    print("delete")
    return redirect('checkout:checkout')





