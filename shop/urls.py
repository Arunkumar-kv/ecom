from django.urls import path,include
from . import views
from django.contrib.auth.models import User
from .models import *
app_name='shop'
urlpatterns = [
    path('',views.allprdocts,name="allproduct"),
    path('<slug:c_slug>/',views.allprdocts,name="cat_allproduct"),
    path('<slug:c_slug>/<slug:product_slug>/',views.productview,name="product"),
    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup'),
    # path('logout/', views.logout, name='logout')

]