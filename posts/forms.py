from django import forms

from posts.models import Hello

class PostForm(forms.ModelForm):
	class Meta:
		model = Hello
		fields = ('user', 'profile', 'title', 'photo')