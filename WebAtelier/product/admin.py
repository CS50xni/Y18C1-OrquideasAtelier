from django.contrib import admin
from .models import Product, Category, ProductImage
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

admin.site.register(Product)
admin.site.register(Category)
