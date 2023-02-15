from django.contrib import admin
from django.shortcuts import render
from django.urls import path

from .models import PostsModel, UrlsModel
from .forms import JsonImportForm


class PostsAdmin(admin.ModelAdmin):
    list_display = ['date', 'content', 'tag']
    list_editable = ['content', 'tag']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload_json/', self.upload_json),]
        return new_urls + urls

    def upload_json(self, request):
        form = JsonImportForm()
        data = {'form': form}
        return render(request, 'admin/upload_json.html', context=data)


class UrlsAdmin(admin.ModelAdmin):
    list_display = ['url']


admin.site.register(PostsModel, PostsAdmin)
admin.site.register(UrlsModel, UrlsAdmin)
