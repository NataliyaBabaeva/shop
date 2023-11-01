from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('',view=views.index_view, name='index'),
    path('product/details/<slug:slug>',view=views.product_detail, name = 'product_detail'),
    path('product/category/<slug:slug>', view=views.category_products_view, name = 'category_products'),
    path('product/favorites/<slug:slug>', view=views.likes, name = 'likes'),
    path('product/favorites/list/',view=views.my_favorites_views, name = 'my_favorites'),
    
]
