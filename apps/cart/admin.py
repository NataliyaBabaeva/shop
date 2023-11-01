from django.contrib import admin
from .models import PromotionalCode,Cart,CartProduct

admin.site.register(PromotionalCode)

class CartProductInline(admin.StackedInline):
    model = CartProduct
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','date_created','status','promo']
    list_filter = ['status']
    search_fields = ['user','date_created']
    inlines = [CartProductInline]

