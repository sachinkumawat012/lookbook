from django.http.response import HttpResponseRedirect, JsonResponse
from .forms import PostForm, CommentForm
from .models import CommentModel, PostModel
from django.shortcuts import  redirect, render
from django.urls import reverse
#Create your views here.
def post(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		#import pdb; pdb.set_trace()
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
		'total_likes': post.like.count(),
		'is_liked': is_liked
	}
	return JsonResponse(data)

def details(request, id):
	#import pdb; pdb.set_trace()
	post = PostModel.objects.get(id=id)
	comments = CommentModel.objects.filter(post_id=post)
	likes = post.like.count()
	form = CommentForm() 
	context = {
		'post': post,
		'form': form,
		'comments': comments,
		'likes': likes
	}
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user_id = request.user
			comment.post_id = post
			comment.save()

	return render(request, 'post/details.html', context) 