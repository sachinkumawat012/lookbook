from .forms import PostForm, CommentForm
from .models import CommentModel, PostModel
from django.shortcuts import  redirect, render

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
