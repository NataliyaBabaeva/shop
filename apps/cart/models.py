from django.db import models
from ..account.models import User
from ..shop.models import Product

CART_STATUSES = (
    ('active','Active'),
    ('closed','Closed'),
    ('finished','Finished'),
    ('waiting','Waiting for payment'),
)


class PromotionalCode(models.Model):
    code = models.CharField(max_length=20)
    discount = models.PositiveSmallIntegerField() 
    
    class Meta:
        verbose_name = "Promo code"
        verbose_name_plural = "Promo codes"
        
        
    def __str__(self):
        return self.code


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    date_finished = models.DateTimeField(null=True)
    promo = models.ForeignKey(PromotionalCode,on_delete=models.SET_NULL, null=True,related_name='carts', blank= True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=CART_STATUSES,default='active')
    
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        
    def __str__(self):
        return self.user.email
    
    
    

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_products')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_products')
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=25)
    quantity = models.PositiveSmallIntegerField(default=1)
    
    
    class Meta:
        verbose_name = "Cart Product"
        verbose_name_plural = "Cart Products"
        
    def __str__(self):
        return f'{self.cart.user.email}-{self.product.name}'
    
    
