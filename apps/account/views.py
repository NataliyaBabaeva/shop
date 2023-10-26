from django.shortcuts import render, get_object_or_404 ,redirect
from .forms import (
    RegisterForm,
    LoginForm,
    ProfileForm ,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:index')  #на домашнюю стр после успешной 
            
            else:
                form.add_error(None, 'wrong login or password')
    
    return render(request, 'login.html', {'form': form, 'errors': form.errors})





def logout_func(request):
    logout(request)
    return redirect('account:login')  #на  стр логинки после выхода из системы  


@login_required
def my_profile(request):
    user = request.user
    
    context = {'user':user}
    
    return render(request=request, template_name='my_profile.html', context=context)


@login_required
def profile_update_view(request):
    user = request.user
    form = ProfileForm(instance=user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        form.save()
    
    context = {'form':form}
    
    return render(request=request, template_name='profile_update.html', context=context)
    
    




     
        