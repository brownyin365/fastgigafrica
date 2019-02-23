from django import forms
from . import models
from .models import Review_Design
from django.contrib.auth.models import User


class CreatePost(forms.ModelForm):
	class Meta:
		model = models.GraphicPost
		fields = ['title','category','sub_category', 'price', 'response_time','requirement','slug','gallery']


class Confirm(forms.ModelForm):
	class Meta:
		model = models.Confirm
		fields = ['subtotal', 'price', 'total', 'quantity']




class CreateReview_Design(forms.ModelForm):
	class Meta:
		model = models.Review_Design
		fields = ['name','author','text','price_rating','location_rating']
