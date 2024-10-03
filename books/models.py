from django.db import models

# Create your models here.

class Book(models.Model):
    
    choses=[
        ('romantic','romantic'),
        ('action','action'),
        ('drama','drama'),
        ('comedy','comedy'),
    ]
    ty=[
        ('trending','trending'),
        ('all books','all books'),
        
    ]
    types=models.CharField(max_length=50,choices=ty ,default='-----')
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5,decimal_places=3)
    description=models.TextField()
    img=models.ImageField(upload_to='images/%y/%m/%d')
    category=models.CharField(max_length=50,choices=choses, default='romantic')
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class Users(models.Model):
    username=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    
    
    def __str__(self):
        return self.username
    