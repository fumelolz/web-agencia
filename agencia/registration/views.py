from django.shortcuts import render,redirect
from .forms import UserCreationFormWithEmail,ProfileForm,EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Profile

class SignUpView(CreateView):
	form_class = UserCreationFormWithEmail
	template_name = 'registration/signup.html'

	def get_success_url(self):
		return reverse_lazy('login') + '?register'

	def get_form(self, form_class=None):
		form = super(SignUpView,self).get_form()
		#Modificar en tiempo real
		form.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Usuario...'})
		form.fields['email'].widget = forms.EmailInput(attrs={'placeholder':'Email...'})
		form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Contraseña...'})
		form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Repite Contraseña...'})
		return form

@method_decorator(login_required,name='dispatch')
class ProfileUpdate(UpdateView):
	form_class = ProfileForm
	success_url = reverse_lazy('profile')
	template_name = 'registration/profile_form.html'

	def get_object(self):
		profile, created = Profile.objects.get_or_create(user=self.request.user)
		return profile

@method_decorator(login_required,name='dispatch')
class EmailUpdate(UpdateView):
	form_class = EmailForm
	success_url = reverse_lazy('profile')
	template_name = 'registration/profile_email_form.html'

	def get_object(self):
		return self.request.user

	def get_form(self, form_class=None):
		form = super(EmailUpdate,self).get_form()
		form.fields['email'].widget = forms.EmailInput(attrs={'placeholder':'Email...'})
		return form