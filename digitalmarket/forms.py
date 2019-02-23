from django import forms
from . import models
from .models import Reviewdigit
from django.contrib.auth.models import User


class CreatePost(forms.ModelForm):
	class Meta:
		model = models.Postdigit
		fields = ['title','category','sub_category', 'response_time', 'price','requirement','gallery', 'delivery']

class Confirm(forms.ModelForm):
	class Meta:
		model = models.Confirm
		fields = ['title', 'subtotal', 'price','requirement','gallery', 'total', 'quantity']



class CreateReview(forms.ModelForm):
	class Meta:
		model = models.Reviewdigit
		fields = ['name','author','text','price_rating','location_rating']
