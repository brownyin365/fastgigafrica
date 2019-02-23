from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse
from .models import Postdigit, Reviewdigit, Confirm
from django.contrib.auth.decorators import login_required
from .import forms
from django.shortcuts import get_object_or_404


# Create your views here.

def post_list(request):
    posts =  Postdigit.objects.all().order_by('date')
    return render(request, 'digital/post_list.html', {'posts': posts})

def post_detail(request):
    post = Postdigit.objects.get()
    return render(request, 'digital/post_detail.html', {'post': post})    

@login_required(login_url='/accounts/login')
def post_create(request):
	if request.method == 'POST':
		form = forms.CreatePost(request.POST,request.FILES)
		if form.is_valid():
			#save post to db
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('posts:list')

	else:	
		form = forms.CreatePost()
	return render(request, 'digital/post_create.html',{'form':form})


@login_required(login_url='/accounts/login')
def post_confirm(request):
	post =  Postdigit.objects.all().order_by('date')
	return render(request, 'digital/post_confirm.html', {'post':post})



def post_review(request):
	return render(request, 'digital/post_review.html', {})