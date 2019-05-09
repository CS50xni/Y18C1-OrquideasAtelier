from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db import models
# Create your views here.
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = "Product/product_list.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context
        
class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "Product/product_detail.html"

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context
