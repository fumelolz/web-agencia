from django.db import models
from django.utils import timezone

class TypePackage(models.Model):
	name = models.CharField(max_length=100,verbose_name="Nombre")
	created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de edición")   
	class Meta:
		verbose_name = "Categoria"
		verbose_name_plural = "Categorias"
		ordering = ['-name']

	def __str__(self):
		return self.name

class Country(models.Model):
	name = models.CharField(max_length=100,verbose_name="Nombre del pais")
	created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de edición")   
	class Meta:
		verbose_name = "Pais"
		verbose_name_plural = "Paises"
		ordering = ['-created']

	def __str__(self):
		return self.name

class Package(models.Model):
	title = models.CharField(max_length=100,verbose_name="Titulo")
	content = models.TextField(verbose_name="Contenido")
	date_posted = models.DateTimeField(verbose_name="Fecha de publicación",default=timezone.now)
	image = models.ImageField(verbose_name="Imagen",upload_to="package",null=True,blank=True)
	country = models.ManyToManyField(Country,verbose_name="Pais",related_name="get_pais")
	tipo = models.ManyToManyField(TypePackage,verbose_name='Categoria',related_name='get_type')
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.title


class Gallery(models.Model):
	image = models.ImageField(verbose_name="Imagen",upload_to="package/galeria",null=True,blank=True)
	paquete = models.ForeignKey(Package,related_name="img",verbose_name="Imagenes que incluye",on_delete=models.CASCADE)

