from django.contrib import admin
from .models import PostsModel


class PostsAdmin(admin.ModelAdmin):
    list_display = ['date', 'content', 'url', 'tag']
    list_editable = ['content', 'url', 'tag']


admin.site.register(PostsModel, PostsAdmin)