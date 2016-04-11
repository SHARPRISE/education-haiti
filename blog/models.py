from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class SuccessStory(models.Model):
        title = models.CharField(max_length=100, default='Story Title')
        slug = models.SlugField(unique=True, max_length=255, default='slug')
        author = models.CharField(max_length=50, default='Author')
        description = models.CharField(max_length=255, default="Success Story description")
        content = models.TextField(default="Story content")
        created = models.DateTimeField(auto_now_add=True, verbose_name="Created on")
        text = models.CharField(max_length=25, default='test')

        def __str__(self):
            return self.title

class Meta:
        ordering = ['-created']

        def __unicode__(self):
                return u'%s' % self.title

        def get_absolute_url(self):
                return reverse('blog.views.success_story', args=[self.slug])