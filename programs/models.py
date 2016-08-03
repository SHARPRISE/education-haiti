from django.db import models
from datetime import datetime

# Create your models here.


class Programs(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, help_text='Where the Program will take place/will be offered')
    description = models.TextField(max_length=255)
    slug = models.SlugField()
    details = models.TextField(max_length=300, help_text='Other details concerning the Program')
    start_date = models.DateField()
    end_date = models.DateField()
    fee = models.IntegerField(null=True, help_text='All fees in Haitian Gourdes HTG')
    phone_contact = models.CharField(max_length=255, help_text='Phone number')
    email_contact = models.EmailField()
    deadline = models.DateField(help_text='Deadline to get in')
    expired_deadline = models.BooleanField(default=False, help_text='did the deadline pass?')
    expired_final = models.BooleanField(default=False, help_text='Did the Program end?')
    picture = models.ImageField('img', upload_to='program_picures/', blank=True)

    def __str__(self):
        return "%s" % self.name + ' ' + self.description

    def deadline_expired(self):
        today = datetime.now()
        if self.deadline == today:
            self.expired_deadline = True
            return self
        elif self.end_date == today:
            self.expired_final = True
            return self

