from django.contrib.auth.models import User
from django.contrib import  auth
from django.http.response import HttpResponse
from django.shortcuts import  render
from django.shortcuts import redirect
from . forms import UserForm, UserProfile
from django.contrib import messages
from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from post.models import Post, Comment
from post.forms import CommentForm


def profile(request):
	#user_posts = Profile.objects.filter(posti=request.user)
	if request.method == "POST":
		form = UserProfile(request.POST, request.FILES)
		#import pdb; pdb.set_trace()
		if form.is_valid():
			profile = form.save(commit =False)
			profile.user = request.user
			profile.save()
			return redirect('main')

	else:
		if request.session.has_key('is_logged'):
			form = UserProfile()
			return render(request, 'myapp/profile.html', {'form':form})
		return redirect('login')


def index(request):
	if request.session.has_key('is_logged'):
		return render(request, 'myapp/index.html')
	return redirect('login')


def home(request):
	return render(request, 'myapp/home.html')



def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST['username']
			password = request.POST['password1']
			
			user = auth.authenticate(username=username, password=password)	
		
			if user is not None:
				auth.login(request, user)
				if request.session.has_key('is_logged'):
				#request.session['is_logged']=True
					return redirect("profile")
					
			else:
		 		return HttpResponse('invailid credentials')
	else:
		request.session['is_logged']=True
		form = UserForm()
		return render(request, 'myapp/register.html', {'form':form})


def login(request): 
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = auth.authenticate(username=username,password=password)	
		
		if user is not None:
			auth.login(request, user)
			request.session['is_logged']=True
			return redirect('main')
		else:
		 	return HttpResponse('invailid credentials')
			
	else:		
		return render(request, 'myapp/login.html')


def logouts(request):
	logout(request)
	return redirect('homepage')

