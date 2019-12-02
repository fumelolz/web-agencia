from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView,ListView
from .models import Testimonials,BannerHero
from blog.models import Post
from packages.models import Package
from django.core.mail import EmailMessage

posts = Post.objects.all().order_by('-created')[:8]
packages = Package.objects.all().order_by('-created')[:8]
banner = BannerHero.objects.get(pk=1)
testimonials = Testimonials.objects.all()[:12]


def sendEmail(email,message):
	#Eviamos email
	email2 = EmailMessage(

			"Urrea Tours: Nuevo mensaje de contacto",
			"De <{}>\n\nEscribio:\n\n{}\n\n".format(email,message),
			"pruebaurreatours@gmail.com",
			["dany_magadan@hotmail.com"],
			reply_to=[email]
		)

	try:
		email2.send()
		return redirect(reverse('home')+"?ok")
	except:
		return redirect(reverse('home')+"?fail")

def home(request):
	context = {
		'banner':banner,
		'posts':posts,
		'packages':packages,
		'testimonials':testimonials,
	}
	
	if request.method == 'POST':
		email = request.POST.get('emailContact')
		message = request.POST.get('message')
		sendEmail(email,message)		

	return render(request,'core/index.html',context)



class AboutView(TemplateView):
	template_name = 'core/about.html'




