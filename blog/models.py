from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class SuccessStory(models.Model):
        title = models.CharField(max_length=100, default='Story Title')
        slug = models.SlugField(unique=True, max_length=255, default='slug')
        author = models.CharField(max_length=50, default='Author')
        description = models.CharField(max_length=255, default="Success Story description")
        content = models.TextField(default="Story content")
        created = models.DateField(auto_now_add=True, verbose_name='Posted on')
        published = models.BooleanField(default=True)
        article_picture = models.ImageField('img', upload_to='media/', blank=True)

        def __str__(self):
            return self.title


        class Meta:
                ordering = ['created']

        def __unicode__(self):
                return u'%s' % self.title

        def get_absolute_url(self):
                return reverse('blog.views.story', args=[self.slug])
