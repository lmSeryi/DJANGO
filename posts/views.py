from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
from datetime import datetime

posts = [
	{
		'title': 'Vías del tren',
		'user': {
		'name':'La Puta Barata',
		'photo': 'https://picsum.photos/id/1027/60/60'
		},
		'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'https://picsum.photos/id/1026/800/800',		
	},
	{
		'title': 'Mont Blac',
		'user': {
		'name':'El Manco',
		'photo': 'https://picsum.photos/id/1026/60/60'
		},
		'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'https://picsum.photos/id/1027/800/800',		
	},
	{
		'title': 'Loneliness',
		'user': {
		'name':'El Negro',
		'photo': 'https://picsum.photos/id/1025/60/60'
		},
		'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'https://picsum.photos/id/1028/800/800',		
	},
]

def list_posts(request):
	return render(request, 'feed.html', {'posts':posts})

# def list_posts(request):
# 	contact = []
# 	for post in posts:
# 		contact.append("""
# 			<p>{name}</p>
# 			<p>{user} - {timestamp}</p>
# 			<figure><img src="{picture}"/></figure>
# 			""".format(**post))
# 	return HttpResponse('<br>'.join(contact))