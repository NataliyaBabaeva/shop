from django.db import models

from django.urls import reverse 
   
    

class Category(models.Model):
    name = models.CharField(max_length=200) 
    slug = models.SlugField(max_length=200,unique=True) #создастся уник индекс
    
    class Meta:
        ordering = ['name'] 
        indexes = [models.Index(fields=['name'])] #индекст по полю name
        verbose_name = 'category' 
        verbose_name_plural = 'categories'
        
    # def get_absolute_url(self): #общепринят способ получ юрл задан объекта,исп шабл кот определила в файле urls.py
    #     return reverse("shop:product_list_by_category", args=[self.slug])
      
    def __str__(self): 
        return self.name



             
class Product(models.Model):
    XS = 'xs'
    S = 's'
    M = 'm'
    L = 'l'
    XL = 'xl'
    SIZES = [
        (XS, 'xs'),
        (S, 's'),
        (M, 'm'),
        (L, 'l'),
        (XL, 'xl'),
    ]
    
    COLORS = [
        ('white', 'White'),
        ('black', 'Black'),
        ('blue', 'Blue')
    ]
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE) #один ко многим
    name = models.CharField(max_length=200)
    slug = models.SlugField('Slug',max_length=200) #слаг для созд url адресов
    description = models.TextField('Description') 
    price = models.DecimalField('Price', max_digits=7,decimal_places=2) 
    available = models.BooleanField(default=True) #булевое значение продукта
    created = models.DateTimeField('Date created',auto_now_add=True) #дата создания проекта
    updated = models.DateTimeField('Date updated',auto_now=True) #дата обновления
    size = models.CharField('Size',max_length=3,choices=SIZES)
    color = models.CharField('Color', max_length=10,choices=COLORS)
    
    class Meta:
        ordering = ['name'] 
        indexes = [models.Index(fields=['id', 'slug']), 
                models.Index(fields=['name']),
                models.Index(fields=['-created']),
                ]
        verbose_name = 'product' 
        verbose_name_plural = 'products'
        
    # def get_absolute_url(self):
    #     return reverse("shop:product_detail", args=[self.id, self.slug])
        
    def __str__(self): 
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image= models.ImageField('image',upload_to='products/',blank=False, default='media\default product.jpg')
    
    class Meta:
        verbose_name = 'product image' 
        verbose_name_plural = 'product images'
    
    def __str__(self) :
        return self.product.name
    
    
class Review(models.Model):
    STARS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5,5),
    ]
    slug = models.SlugField('Slug',max_length=200)
    user = models.ForeignKey('account.User', on_delete=models.SET_NULL,related_name='reviews',null=True, verbose_name='owner')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='reviews', verbose_name='product')
    text = models.TextField('Text')
    stars = models.PositiveSmallIntegerField('Stars',choices=STARS, null= True, blank=True)
    created = models.DateTimeField('Created review', auto_now_add=True)
    
    
    class Meta:
        verbose_name = 'review' 
        verbose_name_plural = 'reviews'
        
class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,related_name='images', verbose_name='Review')
    image = models.ImageField('Image', upload_to='reviews/', null= True, blank= True)
    
    class Meta:
        verbose_name = 'Review image' 
        verbose_name_plural = 'Review images'
        
    
        
        
