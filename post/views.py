from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import PostForm, CommentForm
from .models import Comment, Post, Follower
from django.shortcuts import  redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
import json
#Create your views here.


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit =False)
            profile.user_id = request.user
            profile.save()
            return redirect('index')
    else:
        if request.session.has_key('is_logged'):        
            form = PostForm()
            return render(request, 'post/post.html', {'form':form})
        return redirect('login')


def main(request):
	if request.user.is_authenticated:
		posts = Post.objects.all()
		return render(request, 'post/main.html', {'posts':posts})
	return redirect('login')


def like(request):
	is_liked = False
	post_id = request.GET.get('post_id')
	post = Post.objects.get(id=post_id)
	
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
	else:
		post.likes.add(request.user)
		is_liked = True
	post.save()
	data = {
		'status': 200, 
		'total_likes':post.total_likes(),
		'is_liked': is_liked
	}
	return JsonResponse(data)


def follow(request, id):

	#user_id = request.GET.get('user_id')
	import pdb; pdb.set_trace()
	user = User.objects.get(id=id)
	follower = request.user
	following = Follower.objects.get_or_create(user=user)
	current_following = Follower.objects.get_or_create(another_user=follower)
	
	if user is following:
		Follower.user.remove(following)
	else:
		Follower.user.add(following)
	following.save()
	return JsonResponse(following)


def profile(request, id):
    if request.session.has_key('is_logged'):
        post = Post.objects.filter(id=id)
        return render(request, 'post/profile.html', {'posts':post})
    else:
        return redirect('login')


def details(request, id):
	#import pdb; pdb.set_trace()
	post = Post.objects.get(id=id)
	comments = Comment.objects.filter(post_id=post)
	
	form = CommentForm() 
	context = {
		'post': post,
		'form': form,
		'comments': comments,
	
	}
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user_id = request.user
			comment.post_id = post
			comment.save()

	return render(request, 'post/details.html', context) 
