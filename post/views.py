from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import PostForm, CommentForm
from .models import CommentModel, PostModel, Followers
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


def follow(request, id):
	user = User.objects.get(id=id)
    follower = request.user
    following = Followers.objects.get_or_create(user=user)
    current_following = Followers.objects.get_or_create(another_user=follower)


def profile(request, id):
    if request.session.has_key('is_logged'):
        post = PostModel.objects.filter(id=id)
        return render(request, 'post/profile.html', {'posts':post})
    else:
        return redirect('login')


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


# def profile(request, user_name):
#     user_obj = User.objects.get(name=user_name)
#     session_user = User.objects.get(name=request.session['user'])
#     session_following, create = Followers.objects.get_or_create(user=session_user)
#     following, create = Followers.objects.get_or_create(user=session_user.id)
#     check_user_followers = Followers.objects.filter(another_user=user_obj)

#     is_followed = False
#     if session_following.another_user.filter(name=user_name).exists() or following.another_user.filter(name=user_name).exists():
#         is_followed=True
#     else:
#         is_followed=False
#     param = {'user_obj': user_obj,'followers':check_user_followers, 'following': following,'is_followed':is_followed}
#     if 'user' in request.session:
#         return render(request, 'profile.html', param)
#     else:
#         return redirect('index')


# def follow_user(request, user_name):
#     other_user = User.objects.get(name=user_name)
#     session_user = request.session['user']
#     get_user = User.objects.get(name=session_user)
#     check_follower = Followers.objects.get(user=get_user.id)
#     is_followed = False
#     if other_user.name != session_user:
#         if check_follower.another_user.filter(name=other_user).exists():
#             add_usr = Followers.objects.get(user=get_user)
#             add_usr.another_user.remove(other_user)
#             is_followed = False
#             return redirect(f'/profile/{session_user}')
#         else:
#             add_usr = Followers.objects.get(user=get_user)
#             add_usr.another_user.add(other_user)
#             is_followed = True
#             return redirect(f'/profile/{session_user}')

#         return redirect(f'/profile/{session_user}')
#     else:
#         return redirect(f'/profile/{session_user}')
