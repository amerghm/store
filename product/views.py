from django.shortcuts import render
from product.models import Product
from django.shortcuts import redirect, render
# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/overview.html', {'products': products})



