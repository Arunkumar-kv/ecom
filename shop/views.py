from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from store.models import Cartitem,Cart
from store.views import _cart_id
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib import auth,messages

# Create your views here.
def allprdocts(request,c_slug=None):
    # try:
    #     cart=Cart.objects.get(cart_id=_cart_id(request))
    #     cart_items=Cartitem.objects.filter(cart=cart,active=True)
    #     num_cart=Cart.get_cart_quantity
    # except ObjectDoesNotExist:
    #     pass
    c_page=None
    product_list=None
    if c_slug !=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        product_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        product_list=Product.objects.all().filter(available=True)
        print(product_list)
    return render(request,"index.html",{'c':c_page,'item':product_list})

def productview(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,"product.html",{'pr':product})


# def signup(request):
#     if request.method=='POST':
#
#         email=request.POST['email']
#         pas1=request.POST['password1']
#         pas2=request.POST['password2']
#         if pas1==pas2:
#
#             if User.objects.filter(email=email).exists():
#                 print("email taken")
#                 return redirect("shop:signup")
#
#             user=User.objects.create_user(email=email,password=pas1,)
#             user.save();
#             return redirect("shop:login")
#
#
#         else:
#             return redirect("shop:signup")
#     return render(request,"register.html")
#
# def login(request):
#     if request.method=='POST':
#         email=request.POST['email']
#
#         pas=request.POST['password']
#         user=auth.authenticate(email=email,password=pas)
#
#         if user is not None:
#             auth.login(request,user)
#             return redirect('shop:allproduct')
#         else:
#             messages.info(request,"invalid user")
#             return render(request,"login.html")
#
#     return render(request,'login.html')
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
