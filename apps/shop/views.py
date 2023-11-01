from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# 
# from django.http import JsonResponse
from .models import Category, Product


def index_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,"index.html",context=context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    return render(request, 'product_detail.html', {'product': product})



def category_products_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    
    context = {'category':category, 'products':products}
    
    return render(request,'category_products.html',context=context)



def product_list(request, category_slug=None): 
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True) 
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category) 
    return render(request,'category_products.html',
                  {'category': category,
                   'categories': categories, 
                   'products': products})
    
@login_required
def likes(request, slug):
    product = get_object_or_404(Product, slug = slug)
    user = request.user
    if product in user.favorites.all():
        user.favorites.remove(product)
    else:
        user.favorites.add(product)
        
    return redirect(request.META.get('HTTP_REFERER', '/'))



@login_required
def my_favorites_views(request):
    user = request.user
    favorites = user.favorites.all()
    context = {'favorites':favorites}
    
    return render(request,'favorites.html', context=context)      
    



