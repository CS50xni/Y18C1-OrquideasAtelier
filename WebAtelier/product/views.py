from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from cart.form import CartAddProductForm
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = "Product/product_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

class ProductDetailView(DetailView):
    template_name = "Product/product_detail.html"

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        print(context)
        return context

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all()
