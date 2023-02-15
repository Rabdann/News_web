from django.contrib import admin
from .models import PostsModel, UrlsModel


class PostsAdmin(admin.ModelAdmin):
    list_display = ['date', 'content', 'tag']
    list_editable = ['content', 'tag']


class UrlsAdmin(admin.ModelAdmin):
    list_display = ['url']


admin.site.register(PostsModel, PostsAdmin)
admin.site.register(UrlsModel, UrlsAdmin)
