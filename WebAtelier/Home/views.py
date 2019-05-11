from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product
# Create your views here.

# def index(request):
#     product = Product.objects.all()
#     context = {
#         'products': Product
#     }
#     return render(request,'Home/index.html')

class Home(ListView):
    model = Product
    template_name = 'Home/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        return context


def contact(request):
    return render(request, 'Home/contact.html')
