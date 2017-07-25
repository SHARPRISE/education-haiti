"""education_haiti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap


from blog import urls as blog_urls
from people import urls as people_urls
from mentors import urls as our_mentors_urls
from programs import urls as  programs_urls

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from blog import views

from blog.sitemaps import StaticViewSitemap
from mentors.sitemaps import StaticViewSitemap2

sitemaps = {
    'static': StaticViewSitemap,
    'static2': StaticViewSitemap2,
}



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                                content_type='text/plain')),
    url(r'^blog/', include(blog_urls)),
    url(r'^our_mentors/', include(our_mentors_urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap')
]

if settings.ADMIN_ENABLED:
    urlpatterns.append(url(r'^admin/', admin.site.urls))


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
