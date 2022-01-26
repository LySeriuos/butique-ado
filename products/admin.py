from django.contrib import admin
from .models import Product, Category

# Register your models here.
# if you want to change the order of the columns in the admin
# you can just adjust the order here in the list display attribute

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)