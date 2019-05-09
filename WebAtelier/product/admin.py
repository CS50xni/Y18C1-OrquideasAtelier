from django.contrib import admin
from .models import Product, Category, ProductImage
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    exclude = ['created_at', 'modified_at']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug','created_at','modified']
    inlines = [ProductImageInline]
    exclude = ['created_at']
    class Meta:
        model = Product

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['created_at']
    class Meta:
        model = Category
        

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
