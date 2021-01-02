from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author',)
    prepopulated_fields = {
        "slug": ("title",),
    }

admin.site.register(Post, AuthorAdmin)

# ______________________________________________


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')


admin.site.register(Comment, CommentAdmin)

# _________________________________________________

admin.site.register(Category)

# _________________________________________________


