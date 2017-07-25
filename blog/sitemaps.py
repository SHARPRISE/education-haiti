from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['index', 'resources', 'success_blog', 'apply']

    def location(self, item):
        return reverse(item)
