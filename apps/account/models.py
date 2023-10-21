from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse 


class User(AbstractUser):
    # address = models.CharField(max_length=250)
    slug = models.SlugField('slug', max_length=100,unique=True)
    email = models.EmailField('Email' , unique=True)
    phone_number = models.CharField(max_length=20,null=True)
    
    class Meta:
        verbose_name = 'user' 
        verbose_name_plural = 'users'
        
    def __str__(self): 
        return self.email
    
    
    

