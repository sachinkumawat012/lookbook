from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import PostForm, CommentForm
from .models import CommentModel, Following, PostModel
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
	if request.session.has_key('is_logged'):
		posts = PostModel.objects.all()
		return render(request, 'post/main.html', {'posts':posts})
	return redirect('login')

def like(request):
	is_liked = False
	post_id = request.GET.get('post_id')
	post = PostModel.objects.get(id=post_id)
	
	if post.like.filter(id=request.user.id).exists():
		post.like.remove(request.user)
	else:
		post.like.add(request.user)
		is_liked = True
	post.save()
	data = {
		'status': 200, 
		'total_likes':post.total_likes(),
		'is_liked': is_liked
	}
	return JsonResponse(data)


def follow(request, post_id):
	main_user = request.user
	to_follow = User.objects.get(id=post_id)

	following = Following.objects.filter(user=main_user, followed=to_follow)
	is_following = True if following else False

	if is_following:
		Following.unfollow(main_user, to_follow)
		is_following = False
	else:
		Following.follow(main_user, to_follow)	
		is_following = True	

	context = {

		"is_following": is_following
	}
	response = json.dumps(context)
	return HttpResponse(response, content_type="application/json")


def profile(request, id):
	if request.session.has_key('is_logged'):
		user = User.objects.get(id=id)
	return render(request, 'post/profile.html', {'user':user})


def details(request, id):

	#import pdb; pdb.set_trace()
	post = PostModel.objects.get(id=id)
	comments = CommentModel.objects.filter(post_id=post)
	
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