from .models import Category
from store.models import Cart
def menu_links(request):
     links=Cart.objects.all()
     return dict(link=links)
