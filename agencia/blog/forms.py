from django import forms
from .models import Post

class BlogForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','content','date_posted','image','categories']
		widgets = {
			'categories': forms.CheckboxSelectMultiple(attrs={}),
			'date_posted': forms.DateTimeInput(attrs={}),
		}