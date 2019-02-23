from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=200)   

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Postdigit(models.Model):
    title = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    response_time = models.TimeField(blank=True)
    slug = models.SlugField(max_length=250)
    requirement = models.TextField()
    author = models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    gallery = models.ImageField(null=True, blank=True)
    delivery = models.CharField(max_length=120, default=0)
    

    

    def __str__(self):
        return self.title

    

class Confirm(models.Model):
    title = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    service = models.DecimalField(max_digits=6, decimal_places=5)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=6, decimal_places=4)
    requirement = models.TextField()
    author = models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    gallery = models.ImageField(null=True, blank=True)

 


    def __str__(self):
        return self.title





class Reviewdigit(models.Model):
    name = models.CharField(max_length=1024)
    text = models.TextField()
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    price_rating = models.IntegerField(null=True)
    location_rating = models.IntegerField(null=True)

    def __str__(self):
        return self.name    	