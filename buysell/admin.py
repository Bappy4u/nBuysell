from django.contrib import admin
from .models import Product, Category, Image, Location, LovedProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'condition')


class CategorytAdmin(admin.ModelAdmin):
    list_display = ('category', 'pk')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategorytAdmin)
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(LovedProduct)


# Register your models here.
