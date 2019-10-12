from django.db import models

class User(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=25)
	
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=100)

	isAdmin = models.BooleanField(default = False)

	bio = models.TextField(blank = True)

	birthdate = models.DateField(blank = True, null = True)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.email