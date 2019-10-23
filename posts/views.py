from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from posts.forms import PostForm
from posts.models import Hello
#from django.http import HttpResponse
#from datetime import datetime


@login_required
def list_posts(request):
	posts = Hello.objects.all().order_by('-created')
	return render(request = request,
			template_name = 'posts/feed.html',
				context = {
					'user': request.user,
					'profile': request.user.profile,
					'posts':posts
				},
			)

@login_required
def create_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
		  	form.save()
		# 	return redirect('feed')
	else:
		form = PostForm()

	return render(
			request = request,
			template_name = 'posts/new.html',
			context = {
				'form': form,
				'user': request.user,
				'profile': request.user.profile,
			}
		)

# def list_posts(request):
# 	contact = []
# 	for post in posts:
# 		contact.append("""
# 			<p>{name}</p>
# 			<p>{user} - {timestamp}</p>
# 			<figure><img src="{picture}"/></figure>
# 			""".format(**post))
# 	return HttpResponse('<br>'.join(contact))