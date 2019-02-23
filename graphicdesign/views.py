from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse
from .models import GraphicPost, Confirm
from django.contrib.auth.decorators import login_required
from .import forms


#Views here.
def post_list(request):
    posts =  GraphicPost.objects.all().order_by('date')
    return render(request, 'design/post_list.html', {'posts': posts})

def post_detail(request):
    post = GraphicPost.objects.get()
    return render(request, 'design/post_detail.html', {'post': post})    

# def post(request):
# 	return render(request, 'posts/post.html', {})

@login_required(login_url='/accounts/login')
def post_create(request):
	if request.method == 'POST':
		form = forms.CreatePost(request.POST,request.FILES)
		if form.is_valid():
			#save post to db
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('graphicdesign:list')

	else:	
		form = forms.CreatePost()
	return render(request, 'design/post_create.html',{'form':form})


@login_required(login_url='/accounts/login')
def post_confirm(request):
    post =  GraphicPost.objects.all().order_by('date')
    return render(request, 'design/post_confirm.html',{'post':post})


def post_review(request):
	if request.method == 'POST':
		form = forms.CreateReview(request.POST,)
		if form.is_valid():
			return redirect('design:list')
	else:
		form = forms.CreateReview()		
	return render(request, 'graphicdesign/post_review.html', {'form':form})

