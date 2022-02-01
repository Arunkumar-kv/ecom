from django.urls import path,include
from .views import check
from . import views
from django.contrib.auth.models import User
from .models import *
app_name='checkout'
urlpatterns = [
    path('/',views.check,name="checkout"),
    path('remove/<int:product_id>/',views.check_delete,name="check_delete"),

]