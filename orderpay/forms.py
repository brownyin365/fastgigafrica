from django import forms
from . import models
from django.contrib.auth.models import User
import stripe


class CreateCustomer(forms.ModelForm):
	class Meta:
		model = models.Customer
		fields = ['customer']



