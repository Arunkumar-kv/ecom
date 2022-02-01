from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    class Meta:
         ordering=('name',)
         verbose_name="category"
         verbose_name_plural="categories"


    def __str__(self):
        return '{}'.format(self.name)
    def get_url(self):
        return reverse('shop:cat_allproduct',args=[self.slug])



class Product(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    decription=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
         ordering=('name',)
         verbose_name="product"
         verbose_name_plural="products"


    def __str__(self):
        return '{}'.format(self.name)
    def get_absloute_url(self):
        return reverse('shop:product',args=[self.category.slug,self.slug])