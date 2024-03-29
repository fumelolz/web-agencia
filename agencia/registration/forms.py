from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
	email = forms.EmailField(required=True,help_text="Requerido, 254 caracteres como maximo y debe de ser valido")

	class Meta:
		model = User
		fields = ("username","email","password1","password2")

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('El email ya esta registrado, prueba con otro.')
		return email

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['avatar','bio','link']
		widgets = {
			'bio': forms.Textarea(attrs={'placeholder':'Biografia..'}),
			'link': forms.URLInput(attrs={'placeholder':'Web Personal..'})
		}


class EmailForm(forms.ModelForm):
	email = forms.EmailField(required=True,help_text="Requerido, 254 caracteres como maximo y debe de ser valido")
	class Meta:
		model = User
		fields = ['email']

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if 'email' in self.changed_data:
			if User.objects.filter(email=email).exists():
				raise forms.ValidationError('El email ya esta registrado, prueba con otro.')
		return email