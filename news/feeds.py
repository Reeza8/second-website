
from django.contrib.syndication.views import Feed
from django.urls import reverse
from news.models import News


class LatestEntriesFeed(Feed):
    title = "BizNews latest"
    link = "/rss/feed"
    description = "Updates on changes and additions to BizNews."

    def items(self):
        return News.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:70]

