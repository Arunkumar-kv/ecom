from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from store.models import Cart,Cartitem

class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    popup_response_template = {'slug':('name',)}
admin.site.register(Category,categoryadmin)



class productadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available']
    list_editable = ['price','stock','available']
    popup_response_template = {'slug':('name',)}
    list_per_page =20
admin.site.register(Product,productadmin)
admin.site.register(Cart)
admin.site.register(Cartitem)

