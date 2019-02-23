from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
	customer = models.EmailField(User, default=None)
	

    


   

