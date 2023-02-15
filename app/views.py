import json

import snscrape.modules.telegram as telegram
from rest_framework import viewsets

from app.models import PostsModel
from app.serializers import PostsSerializer


def get_posts_yandex(name_channel):
    scraper = telegram.TelegramChannelScraper(name_channel)
    posts = []

    for i, post in enumerate(scraper.get_items(), 1):
        if i >= 11:
            break
        posts.append(
            {'pk': i, 'model': 'app.postsmodel',
             'fields': {'date': post.date, 'content': post.content, 'url': post.outlinks, 'tag': post.url[15:33]}})

    result = json.dumps(posts, ensure_ascii=False, default=str)
    with open('yandex.json', 'w') as f:
        f.write(result)
    return result


def get_posts_ozon(name_channel):
    scraper = telegram.TelegramChannelScraper(name_channel)
    posts = []

    for i, post in enumerate(scraper.get_items(), 1):
        if i >= 11:
            break
        posts.append(
            {'pk': i, 'model': 'app.postsmodel',
             'fields': {'date': post.date, 'content': post.content, 'url': post.outlinks, 'tag': post.url[15:30]}})

    result = json.dumps(posts, ensure_ascii=False, default=str)
    with open('ozon.json', 'w') as f:
        f.write(result)
    return result


class PostsViewSet(viewsets.ModelViewSet):
    queryset = PostsModel.objects.all()
    serializer_class = PostsSerializer
