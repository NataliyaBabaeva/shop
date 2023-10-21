from django.shortcuts import render, get_object_or_404 ,redirect
from .forms import (
    RegisterForm,
    LoginForm,
)
from django.contrib.auth import authenticate, login, logout

# список товаров или фильтрация по заданной категории
# def product_list(request, category_slug=None): 
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category) 
#     return render(request,'account/product/detail.html', {'category': category,
# 'categories': categories, 'products': products})



# def all_product(request):
#     products = Product.objects.all() под вопросом

# def index_viev(request):
#     return render(request,"index.html")

# 3 функц регистр, логинка , логаут
# потом в url регистр их

def register_func(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request,'register.html', {'massage': 'User registered','form':form})
        else:
            return render(request,'register.html', {'errors': form.errors,'form':form})
    else:
        
        return render(request, 'register.html',{'form': form})
    
    
def login_func(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index.html')  #на домашнюю стр после успешной 
            else:
                form.add_error(None, 'wrong login or password')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index.html')  #на дом стр после выхода из системы   

     
        