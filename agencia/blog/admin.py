from django.contrib import admin
from blog.models import Category,Post

class CategoryAdmin(admin.ModelAdmin):
	readonly_fields = ('created','updated')
class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('created','updated')
	list_display = ('title','author','date_posted','post_categories')
	ordering = ('author','date_posted')
	search_fields = ('id','title','content','author__username','categories__name')
	date_hierarchy = 'date_posted'
	list_filter = ('categories','date_posted')

	def post_categories(self,obj):
		return ",".join([c.name for c in obj.categories.all().order_by("name")])
	post_categories.short_description = "Categorias"


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
