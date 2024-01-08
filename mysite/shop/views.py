from django.shortcuts import render, get_object_or_404
from .models import Product, Brand


def home(request):
    products = Product.objects.all().order_by('-id')[:5]
    title = 'Главная страница'
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'shop/home.html', context)

def about(request):
    title = 'О Нас'
    context = {
        'title': title,
    }
    return render(request, 'shop/about.html', context)

def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'shop/contact.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.increase_popularity(amount=1)
    context = {
        'product': product,
    }
    return render(request, 'shop/product_detail.html', context)

def product_list(request):
    brand_id = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    products = Product.objects.all().order_by('-id')

    brands = Brand.objects.all()
    if brand_id:
        products = products.filter(brand_id=brand_id)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    sort = request.GET.get('sort', 'popularity')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'popularity':
        products = products.order_by('-popularity_score')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    title = 'Товары'
    context = {
        'title': title,
        'products': products,
        'brands': brands,
    }
    return render(request, 'shop/product_list.html', context)


def product_search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query)
    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'shop/home.html', context)
