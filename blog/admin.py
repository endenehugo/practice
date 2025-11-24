from django.contrib import admin

from .models import Blog, BlogCategory, BlogComment


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_time', 'category', 'author', 'content']

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'pub_time', 'blog', 'author']

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)