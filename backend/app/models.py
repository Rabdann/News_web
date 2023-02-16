from django.db import models


class PostsModel(models.Model):
    date = models.DateTimeField(verbose_name='Дата')
    content = models.TextField(max_length=3000, verbose_name='Контент')
    tag = models.CharField(max_length=100, verbose_name='Тэг')

    def __str__(self):
        return f'{self.tag} - {self.content}' or ''

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['date', 'tag']


class UrlsModel(models.Model):
    url = models.CharField(max_length=2000)
    post = models.ForeignKey(PostsModel, on_delete=models.CASCADE, verbose_name='Пост', related_name='posts')

    class Meta:
        verbose_name = 'Вложенный url'
        verbose_name_plural = 'Вложенные url'

