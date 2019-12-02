from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from blog.models import Post
from django.views.generic.list import MultipleObjectMixin

# class ProfileListView(DetailView):
# 	model = Profile
# 	template_name="profiles/profile_list.html"

class ProfileDetailView(DetailView):
	model = Profile
	template_name = "profiles/profile_detail.html"

	# def get_context_data(self,**kwargs):
	# 	object_list = Post.objects.all().filter(author__username=self.get_object())
	# 	context = super(ProfileDetailView,self).get_context_data(object_list=object_list, **kwargs)

	def get_object(self):
		return get_object_or_404(Profile,user__username=self.kwargs['username'])

		
