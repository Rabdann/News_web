from django.db import models


class PostsModel(models.Model):
    date = models.DateTimeField(verbose_name='Дата')
    content = models.TextField(max_length=3000, verbose_name='Контент')
    url = models.CharField(max_length=100, verbose_name='Вложенные url')
    tag = models.CharField(max_length=100, verbose_name='Тэг')

    def __str__(self):
        return f'{self.tag} - {self.content}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['date', 'tag']