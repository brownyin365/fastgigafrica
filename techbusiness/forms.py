from django import forms
from . import models
from .models import Reviewtech
from django.contrib.auth.models import User


class CreatePost(forms.ModelForm):
	class Meta:
		model = models.Posttech
		fields = ['title','category','sub_category', 'response_time', 'price','requirement','gallery', 'delivery']



class CreateReview(forms.ModelForm):
	class Meta:
		model = models.Reviewtech
		fields = ['name','author','text','price_rating','location_rating']
