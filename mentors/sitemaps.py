from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class StaticViewSitemap2(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['our_mentors']

    def location(self, item):
        return reverse(item)
