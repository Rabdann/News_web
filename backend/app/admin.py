import json

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django.contrib import messages

from .models import PostsModel, UrlsModel
from .forms import JsonImportForm


class UrlsInline(admin.StackedInline):
    model = UrlsModel
    extra = 0


class PostsAdmin(admin.ModelAdmin):
    inlines = [UrlsInline]
    list_display = ['date', 'content', 'tag']
    list_editable = ['tag']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload_json/', self.upload_json), ]
        return new_urls + urls

    def upload_json(self, request):
        if request.method == 'POST':
            json_file = request.FILES['json_upload']
            if not json_file.name.endswith('.json'):
                messages.warning(request, 'Загружен неправильный тип файла, загрузите тип - (json)')
                return HttpResponseRedirect(request.path_info)
            file_data = json.load(json_file)
            for field in file_data:
                post, _ = PostsModel.objects.update_or_create(
                    date=field['fields']['date'],
                    content=field['fields']['content'],
                    tag=field['fields']['tag'],
                )
                urls = field['fields']['url']

                for url in urls:
                    UrlsModel.objects.create(post=post, url=url)

            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = JsonImportForm()
        data = {'form': form}
        return render(request, 'admin/upload_json.html', context=data)


class UrlsAdmin(admin.ModelAdmin):
    list_display = ['url']


admin.site.register(PostsModel, PostsAdmin)
admin.site.register(UrlsModel, UrlsAdmin)
