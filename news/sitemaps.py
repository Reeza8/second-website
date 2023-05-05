from django.contrib.sitemaps import Sitemap
from news.models import News,Category


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return News.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.published_date