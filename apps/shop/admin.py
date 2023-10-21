from django.contrib import admin
from .models import Category,Product,ProductImage,Review,ReviewImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] 
    prepopulated_fields = {'slug': ('name',)} #исп что указ поля кот уст автом с исп значен др полей,удобно для генерир слагов
 
 
# @admin.register(ProductImage)ы
class ProductImageInline(admin.StackedInline):
    model = ProductImage 


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated'] # любое поля list_editable должно быть указано в атрибуте,т.тк редакт можно только отображ поля
    list_filter = ['price','available', 'created', 'updated'] 
    list_editable = ['price', 'available'] # задает поля кот мож редакт наход на стр отображ списка на сайте администриров,позвол редакт неск стр одновремменно
    search_fields = ['slug','name','description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline,]


class ReviewImageInline(admin.StackedInline):
    model=ReviewImage
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['slug', 'product', 'user', 'stars']
    list_filter = ['stars', 'product', 'user']
    sortable_by = [' created']
    search_fields = ['slug', 'text']
    inlines = [ReviewImageInline,]


# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Product,ProductAdmin)
# admin.site.register(Review,ReviewAdmin)

