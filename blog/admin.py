from django.contrib import admin
from .models import Post, Comment
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish', 'status', 'author')
	list_filter = ('status', 'author', 'publish', 'created')
	search_fields = ('title', 'body')
	raw_id_fields = ('author',)
	ordering = ('publish', 'status')
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'publish'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('post', 'name', 'email', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('body', 'name', 'email')
