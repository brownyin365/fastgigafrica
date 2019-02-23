from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse
from .models import PostVideo, ReviewVideo
from django.contrib.auth.decorators import login_required
from .import forms


# Create your views here.
def post_list(request):
    posts =  PostVideo.objects.all().order_by('date')
    return render(request, 'video/post_list.html', {'posts': posts})

def post_detail(request):
    post = PostVideo.objects.get()
    return render(request, 'video/post_detail.html', {'post': post})    


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
	return render(request, 'video/post_create.html',{'form':form})

@login_required(login_url='/accounts/login')
def post_confirm(request):
	post = PostVideo.objects.all().order_by('date')
	 # total = YourModel.objects.all().aggregate(tot=Sum('total'))['tot']
  #       return post
	return render(request, 'video/post_confirm.html', {'post':post})


def post_review(request):
	return render(request, 'video/post_review.html', {})