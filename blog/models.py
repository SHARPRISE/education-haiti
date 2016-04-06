from django.db import models

# Create your models here.

class SuccessStory(models.Model):
        title = models.CharField(max_length=100)
        author = models.CharField(max_length=50)
        content = models.TextField(null=True)
        date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Posted on")

        def __str__(self):
            return self.title