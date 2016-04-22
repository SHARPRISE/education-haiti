from django.db import models
from django.contrib.auth.models import AbstractUser

from hashlib import sha1
# Create your models here.

# User model
class User(AbstractUser):
    RANK_CHOICES = (
        ('A', 'mentor'),
        ('B', 'mentee'),
    )

    rank            = models.CharField(max_length=255, choices=RANK_CHOICES, default=RANK_CHOICES[1], null=True,)
    hidden          = models.BooleanField(default = False)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return "%s" % self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

User._meta.get_field('email')._unique = True


# HIGHSCHOOLS = ()
# UNIVERSITIES = ()


class Mentee(models.Model):
    user        = models.OneToOneField(User)
    picture     = models.ImageField(upload_to="profile_images", blank=True)
    #graduating = models.DateField() OR highschool = models.CharField(max_lenght=255, choices=HIGHSCHOOLS, required=True)

    def __str__(self):
        return "mentee's profile %s" % self.user.email

# Mentor model
class Mentor(models.Model):

    user        = models.OneToOneField(User)
    picture     = models.ImageField(upload_to="profile_images", blank=True)

    biography   = models.TextField()
    #graduating  = models.DateField() or universities = models.CharField(max_lenght=255, choices=UNIVERSITIES, required=True)

    mentees     = models.ManyToManyField(Mentee)
    hidden      = models.BooleanField(default=False)

    def __str__(self):
        return "mentor's profile %s" % self.user.email
