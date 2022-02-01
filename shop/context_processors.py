from .models import Category
from store.models import Cart
def menu_link(request):
     links=Category.objects.all()
     return dict(links=links)
