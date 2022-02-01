from django.db import models
from shop.models import *
# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=50,blank=True)
    date_add=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['date_add']

    def __str__(self):
        return '{}'.format(self.cart_id)
    @property
    def get_cart_total(self):
        cartitems=self.cartitem_set.all()
        total=sum([product.get_subtotal for product in cartitems])
        return total
    @property
    def get_cart_quantity(self):
        cartitems=self.cartitem_set.all()
        quantity=sum([product.quantity for product in cartitems])
        return quantity

class Cartitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='Cartitem'
    @property
    def get_subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):

        return '{}'.format(self.product)

    def get_u(self):
        return reverse('store:cart_remove', args=[self.product.id])
    def get_del(self):
        return reverse('store:cart_delete', args=[self.product.id])
    def get_delc(self):
        return reverse('checkout:check_delete', args=[self.product.id])