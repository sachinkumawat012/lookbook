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


def follow(request,):

	user_id = request.GET.get('user_id')                            # to be followed 
	follow_user = User.objects.get(id=user_id)
	user = request.user                                              #current user
	follower = Follower.objects.get_or_create(user=user)[0]
	is_following = False
	
	if follower.another_user.filter(id=follow_user.id).exists():
		follower.another_user.remove(follow_user)
	else:
		follower.another_user.add(follow_user)
		is_following = True
	data = {
		"is_following": is_following,

	}
	return JsonResponse(data)


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
