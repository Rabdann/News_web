# Generated by Django 4.1.7 on 2023-02-16 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_post_urlsmodel_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Вложенный url',
                'verbose_name_plural': 'Вложенные url',
            },
        ),
        migrations.RenameModel(
            old_name='PostsModel',
            new_name='Post',
        ),
        migrations.DeleteModel(
            name='UrlsModel',
        ),
        migrations.AddField(
            model_name='urls',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='app.post', verbose_name='Пост'),
        ),
    ]
