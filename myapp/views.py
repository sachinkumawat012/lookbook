from django.contrib.auth.models import User
from django.contrib import  auth
from django.http.response import HttpResponse
from django.shortcuts import  render
from django.shortcuts import redirect
from . forms import NewUserForm, UserProfile
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import Profile

def profile(request):
	form = UserProfile()
	return render(request, 'myapp/profile.html')


def index(request):
	if request.session.has_key('is_logged'):
		return render(request, 'myapp/index.html')
	return redirect('login')


def home(request):
	return render(request, 'myapp/home.html')



def register(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully Register")
			return redirect('login')         

	else:
		form = NewUserForm()
		return render(request, 'myapp/register.html', {'form':form})


def login(request): 
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = auth.authenticate(username=username,password=password)	
		
		if user is not None:
			auth.login(request, user)
			request.session['is_logged']=True
			return redirect('index')
		else:
		 	return HttpResponse('invailid credentials')
			
	else:		
		return render(request, 'myapp/login.html')