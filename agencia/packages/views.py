from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Package

international = Package.objects.filter(tipo__id=1)
class PackagesHomeView(ListView):
	model = Package
	template_name = 'packages/packages.html'
	context_object_name = 'packages'
	paginate_by = 8

class PackagesInternationalView(ListView):
	model = Package
	context_object_name = 'packages'
	paginate_by = 8
	template_name = 'packages/packages-international.html'

	def get_queryset(self):
		return Package.objects.filter(tipo__id=1)

class PackagesNationalView(ListView):
	model = Package
	context_object_name = 'packages'
	paginate_by = 8
	template_name = 'packages/packages-national.html'

	def get_queryset(self):
		return Package.objects.filter(tipo__id=2)

class PackagesSingleView(DetailView):
	model = Package
	template_name = 'packages/packages-single.html'