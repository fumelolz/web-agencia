from django.db import models

class BannerHero(models.Model):
	title = models.CharField(verbose_name='Titulo',max_length=200)
	subtitle = models.TextField(verbose_name='Subtitulo')
	buttonlink = models.URLField(verbose_name='Link')

	class Meta:
		verbose_name = 'Banner Hero'
		verbose_name_plural = 'Banner Hero'

	def __str__(self):
		return self.title

class Testimonials(models.Model):
	name = models.CharField(verbose_name='Nombre de la persona',max_length=200)
	content = models.TextField(verbose_name='Contenido')
	stars = models.PositiveSmallIntegerField(verbose_name='Estrellas')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Testimonio'
		verbose_name_plural = 'Testimonios'