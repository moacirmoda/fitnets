from django import forms
from models import *

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('created', 'creator', 'updater', 'updated', 'like', 'non_like', 'parent', 'user')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('created', 'creator', 'updater', 'updated', 'like', 'non_like')
