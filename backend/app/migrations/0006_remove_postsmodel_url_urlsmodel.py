# Generated by Django 4.1.7 on 2023-02-15 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_postsmodel_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postsmodel',
            name='url',
        ),
        migrations.CreateModel(
            name='UrlsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.postsmodel', verbose_name='Вложенные url')),
            ],
            options={
                'verbose_name': 'Вложенный url',
                'verbose_name_plural': 'Вложенные url',
            },
        ),
    ]
