from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='profiles',null=True,blank=True)
	bio = models.TextField(null=True,blank=True)
	link = models.URLField(max_length=200,null=True,blank=True)

	def __str__(self):
		return f'{self.user.username} Profile'
	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)
	# 	if self.avatar.path:
	# 		img = Image.open(self.avatar.path)
	# 		if img:
	# 			if img.height > 300 or img.width > 300:
	# 				output_size = (300,300)
	# 				img.thumbnail(output_size)
	# 				img.save(self.avatar.path)
		
			

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
	if kwargs.get('created', False):
		Profile.objects.get_or_create(user=instance)
		print("Se creo un usuario y su perfil")