from .models import Category,Product


def categories_processor(request):
    categories = Category.objects.all()
    
    context = {'categories': categories}
    
    return context



def likes_count(request):
    user = request.user
    favorites = user.favorites.count()
    context = {'favorites_count':favorites}
    
    return context