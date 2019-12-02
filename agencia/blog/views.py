from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Post,Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView,UpdateView,DeleteView
from .forms import BlogForm
from django.db.models import Q
from django.contrib.auth.mixins import (
LoginRequiredMixin, #Import para validar que el usuaro este logeado
UserPassesTestMixin #Import para validar que el usuario sea el dueño del blog
)
from core.views import sendEmail


#Clase para mostrar todos los blogs
class BlogHomeListView(ListView):
	model = Post
	template_name = "blog/blog-home.html"
	context_object_name = 'posts'
	paginate_by = 5
	ordering = '-date_posted'

	def get_context_data(self,**kwargs):
		context = super(BlogHomeListView,self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all().order_by('name')
		context['post_views_list'] = Post.objects.all().order_by('-views')[:12]
		return context

	def get_queryset(self):
		if self.request.GET.get('search-item'):
			query = self.request.GET.get('search-item')
			return Post.objects.filter(title__icontains=query)
		return Post.objects.all()

#Clase para mostrar todos los blogs del usuario
class BlogUserListView(ListView):
	queryset = Post
	template_name = "blog/blog-user-list.html"
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		if self.request.GET.get('search-item'):
			query = self.request.GET.get('search-item')
			return Post.objects.filter(title__icontains=query)
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

	def get_context_data(self,**kwargs):
		context = super(BlogUserListView,self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all().order_by('name')
		context['post_views_list'] = Post.objects.all().order_by('-views')[:12]
		return context

#Clase para mostrar todos los blogs de la categoria
class BlogCategoryListView(ListView):
	queryset = Category
	template_name = "blog/blog-category-list.html"
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		if self.request.GET.get('search-item'):
			query = self.request.GET.get('search-item')
			return Post.objects.filter(title__icontains=query)
		categorie = get_object_or_404(Category,name=self.kwargs.get('categoryname'))
		posts = Category.objects.get(name=categorie)
		return posts.get_posts.all()

	def get_context_data(self,**kwargs):
		context = super(BlogCategoryListView,self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all().order_by('name')
		context['post_views_list'] = Post.objects.all().order_by('-views')[:12]
		return context


#Clase para mostrar todos los blogs de la busqueda
class BlogSearchListView(ListView):
	queryset = Post
	template_name = "blog/blog-search-list.html"
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		if self.request.GET.get('search-item'):
			query = self.request.GET.get('search-item')
			return Post.objects.filter(title__icontains=query)
		search = get_object_or_404(Post,name=self.kwargs.get('search'))
		print(search)
		posts = Category.objects.get(name=categorie)
		return posts.get_posts.all()

	def get_context_data(self,**kwargs):
		context = super(BlogSearchListView,self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all().order_by('name')
		context['post_views_list'] = Post.objects.all().order_by('-views')[:12]
		return context


#Clase para mostrar en una sola pagina de blog a detalle
class BlogDetailView(DetailView):
	model = Post
	template_name = "blog/single-blog.html"

	def view(self):
		d = self.get_object()
		if self.request.user.is_authenticated:
			d.views += 1
			d.save()

	def get(self,*args,**kwargs):
		self.view()
		return super(BlogDetailView,self).get(self,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(BlogDetailView,self).get_context_data(**kwargs)
		context['post_views_list'] = Post.objects.all().order_by('-views')[:4]
		context['categories'] = Category.objects.all().order_by('name')
		return context

	def get_queryset(self):
		if self.request.GET.get('search-item'):
			query = self.request.GET.get('search-item')
			return Post.objects.filter(title__icontains=query)
		return Post.objects.all()

		

#Clase para mostrar el formulario para crear un blog
class BlogCreateView(LoginRequiredMixin,CreateView):
	form_class = BlogForm
	model = Post
	template_name = 'blog/post_form_create.html'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

#Clase para mostrar el formulario y editar un blog creado
class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	form_class = BlogForm
	model = Post
	template_name = 'blog/post_form_update.html'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#Definimos una funcion para comparar los user del post y del que edita
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True 
		return False	

	def get_queryset(self):
		if self.request.GET.get('search-item'):
			query = self.request.GET.get('search-item')
			return Post.objects.filter(title__icontains=query)
		return Post.objects.all()

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = reverse_lazy('blog-home')

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#Definimos una funcion para comparar los user del post y del que edita
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True 
		return False

	def get_queryset(self):
		if self.request.GET.get('search-item'):
			query = self.request.GET.get('search-item')
			return Post.objects.filter(title__icontains=query)
		return Post.objects.all()


# # def blog_home(request):
# # 	context = {
# # 		'posts': Post.objects.all(),
# # 		'categorys': Category.objects.order_by('name').all()
# # 	}
# # 	return render(request,'blog/blog-home.html',context)

# def blog_single(request):
# 	return render(request,'blog/single_blog.html')
