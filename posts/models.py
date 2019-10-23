from django.db import models
from django.contrib.auth.models import User

class Hello(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	profile = models.ForeignKey('user.Profile', on_delete = models.CASCADE)
	
	title = models.CharField(max_length = 255)
	photo = models.ImageField(upload_to = 'posts/phots')

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return self.user.username

