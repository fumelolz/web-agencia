from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField
from django.urls import reverse


#Modelo de categorias
class Category(models.Model):
	name = models.CharField(max_length=100,verbose_name="Nombre")
	created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "categoria"
		verbose_name_plural = "categorias"
		ordering = ['-created']

	def __str__(self):
		return self.name

#Modelo de Blogs
class Post(models.Model):
	title = models.CharField(max_length=100,verbose_name="Titulo")
	content = RichTextField(verbose_name="Contenido")
	date_posted = models.DateTimeField(verbose_name="Fecha de publicación",default=timezone.now)
	image = models.ImageField(verbose_name="Imagen",upload_to="blog",null=True,blank=True)
	views = models.PositiveIntegerField(default=0)
	author = models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE,related_name='user_posts')
	categories = models.ManyToManyField(Category,verbose_name="Categorías",related_name="get_posts")
	created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de edición")

	class Meta:
		verbose_name = "entrada"
		verbose_name_plural = "entradas"
		ordering = ['-created']

	def __str__(self):
		return self.title

	#Definimos un metodo para obtener una url absoluta, para redirigir cuando se crea un post
	def get_absolute_url(self):
		return reverse('blog-detail',kwargs={'pk':self.pk})
