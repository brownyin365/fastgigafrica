from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse
from .models import Posttech, Reviewtech
from django.contrib.auth.decorators import login_required
from .import forms

# Create your views here.

def post(request):
    posts =  Posttech.objects.all().order_by('date')
    return render(request, 'techbusiness/post_list.html', {'posts': posts})


def post_list(request):
    posts =  Posttech.objects.all().order_by('date')
    return render(request, 'tech/post_list.html', {'posts': posts})

def post_detail(request):
    post = Posttech.objects.get()
    return render(request, 'tech/post_detail.html', {'post': post})    


@login_required(login_url='/accounts/login')
def post_create(request):
	if request.method == 'POST':
		form = forms.CreatePost(request.POST,request.FILES)
		if form.is_valid():
			#save post to db
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('techbusiness:list')

	else:	
		form = forms.CreatePost()
	return render(request, 'tech/post_create.html',{'form':form})


@login_required(login_url='/accounts/login')
def post_confirm(request):
	post = Posttech.objects.all().order_by('date')
	return render(request, 'tech/post_confirm.html', {'post':post})


def post_review(request):
	return render(request, 'posts/post_review.html', {})