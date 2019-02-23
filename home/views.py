from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import views


# Create your views here.

def index(request):
	return render(request, 'index.html', {})


def dashboard(request):
	return render(request, 'dashboard.html', {})	


def offerapost(request):
	return render(request, 'offerapost.html', {})

def manageorder(request):
	return render(request, 'manageorder.html', {})


@login_required(login_url='/accounts/login')
def orderconfirm(request):
	return render(request, 'orderconfirm.html', {})	


def jobdetails(request):
	return render(request, 'jobdetails.html', {})	

def offerapost2(request):
    return render(request, 'home/home/offerapost2', {})

def offerapost3(request):
    return render(request, 'home/home/offerapost3', {})

def offerapost4(request):
    return render(request, 'home/home/offerapost4', {})     


