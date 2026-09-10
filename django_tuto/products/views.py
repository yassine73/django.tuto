from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    # item = Product.objects.get(name='oppo')
    item = str(Product.objects.count())
    return render(request, "products/product.html", {'product': item})

def products(request):
    # items = Product.objects.all()
    # items = Product.objects.filter(category='phone')
    # items = Product.objects.order_by('price')
    # items = Product.objects.exclude(category = '')
    # items = Product.objects.filter(name__exact = 'oppo')
    # items = Product.objects.filter(name__contains = 'oppo')
    # items = Product.objects.filter(price__in = [10, 100, 3])
    items = Product.objects.filter(price__range = [100, 1000])
    context = {
        "products": items,
    }
    return render(request, "products/products.html", context=context)

