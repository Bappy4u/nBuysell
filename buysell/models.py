from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver


class Image(models.Model):
    image = models.ImageField(upload_to='products')


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return str(self.category)


class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.TextField(max_length=100)
    price = models.IntegerField()
    condition_opt = (
        ('used', 'Used'),
        ('new', 'New'),
    )
    post_cat = (
        ('sell', 'Sell'),
        ('buy', 'Buy')
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    condition = models.CharField(max_length=10, choices=condition_opt)
    post_category = models.CharField(max_length=10, choices=post_cat)
    details = models.TextField(max_length=300)
    is_negotiable = models.BooleanField(default=True)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True)
    uploaded_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.TextField(max_length=13)
    url = models.TextField(max_length=40)
    image = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['uploaded_time']


class LovedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ManyToManyField(Product, blank=True)


@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    if kwargs.get('created'):
        LovedProduct.objects.create(user=kwargs.get('instance'))
