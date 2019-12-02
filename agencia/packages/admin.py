from django.contrib import admin
from .models import Package,Gallery,Country,TypePackage
from django.db import models
from django import forms
from django.forms import CheckboxSelectMultiple,CheckboxInput,RadioSelect

class GalleryInlineAdmin(admin.StackedInline):
	model = Gallery
	verbose_name_plural = "Galeria de imagenes"
	extra = 1

class PackageAdmin(admin.ModelAdmin):
	inlines = [ GalleryInlineAdmin, ]

	# formfield_overrides = {
 #        models.ManyToManyField: {'widget': RadioSelect},
 #    }

admin.site.register(Package,PackageAdmin)
admin.site.register(Country)
admin.site.register(TypePackage)
