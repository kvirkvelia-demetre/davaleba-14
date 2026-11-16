from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'home.html')


def products(request):
    products = Product.objects.all()

    return render(request, 'products.html', {
        'products': products
    })


def detail_product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'detail_product.html', {
        'product': product
    })