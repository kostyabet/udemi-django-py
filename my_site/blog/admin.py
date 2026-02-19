from django.contrib import admin
from .models import Author, Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)