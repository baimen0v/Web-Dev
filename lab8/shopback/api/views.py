from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Category,Product
from django.shortcuts import redirect

def home(request):
    return redirect('product_list')

def product_list(request):
    products = Product.objects.all()
    data = {'products':list(products.values())}
    data = {'products': list(products.values)}
    return JsonResponse(data)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    data = {'product': {
        'name':product.name,
        'price':product.price,
        'description':product.description,
        'count' :product.count,
        'is_active': product.is_active

    }}
    return JsonResponse(data)

def category_list(request):
    categories = Category.objects.all()
    data = {'categories': list(categories.values())}
    return JsonResponse(data)

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    data = {'category':{
        'name':category.name
    }}
    return JsonResponse(data)

def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    data = {'products': list(products.values())}
    return JsonResponse(data)

# Create your views here.
