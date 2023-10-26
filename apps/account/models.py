from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse 
from django.db import IntegrityError
from django.template.defaultfilters import slugify


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
    
    def save(self, *args, **kwargs):
        while True:
            self.slug = slugify(self.username)
            try:
                return super().save(*args, **kwargs)
            except IntegrityError:
                continue

    

