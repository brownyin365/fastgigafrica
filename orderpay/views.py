from django.shortcuts import render, redirect, HttpResponse
import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
# from .models import Customer
from .import forms


#Stripe APi keys
stripe.api_key = settings.STRIPE_SECRET_KEY 
STRIPE_PUBLISHABLE_KEY = 'pk_test_UJpylN6QVgb1CkutBjo79Jfy'

stripe.api_key = "sk_test_QNqDISb8rzgXnOkbQBS9kdaL"



class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == 'POST':
        # customer = stripe.Customer.create(email=request.form['stripeEmail'])

        customer = stripe.Customer.create(description='test')

        token = request.POST['stripeToken']


        charge = stripe.Charge.create(
                amount=999,
                currency='usd',
                description='Example charge',
                # receipt_email='jenny.rosen@example.com',
                source=token,
            )
    return render(request,'orderpay/charge.html',{})




