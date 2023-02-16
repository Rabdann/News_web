import json

import snscrape.modules.telegram as telegram


def get_posts_from_yandex_or_ozon(name_channel):
    scraper = telegram.TelegramChannelScraper(name_channel)
    posts = []

    for i, post in enumerate(scraper.get_items(), 1):
        if i >= 11:
            break
        posts.append(
            {'model': 'app.postsmodel',
             'fields': {'date': post.date, 'content': post.content, 'url': post.outlinks,
                        'tag': post.url[15:33] if name_channel == 'market_marketplace' else post.url[15:30]}})
    result = json.dumps(posts, ensure_ascii=False, default=str)
    with open(f'{name_channel}.json', 'w') as f:
        f.write(result)
    return result
