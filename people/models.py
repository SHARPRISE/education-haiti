from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

from hashlib import sha1
# Create your models here.

UNIVERSITIES = (
    ('1', 'Illinois State University'),
    ('2', 'Mount Holyoke College'),
    ('3', 'University of Notre Dame'),
    ('4', 'Columbia University'),
    ('5', 'Cornell University'),
    ('6', 'Ecole Polytechnique de Montreal'),
    ('7', 'Georgia Tech University'),
    ('8', 'Harvard University'),
    ('9', 'Louisiana State University'),
    ('10', 'Massachusettes Institute of Technology'),
    ('11', 'McGill University'),
    ('12', 'Moncton University'),
    ('13', 'Southern University'),
    ('14', 'Tufts University'),
    ('15', 'University of Michigan'),
    ('16', 'University of Pennsyvalnia'),
    ('17', 'Cooper Union'),
    ('18', 'St Leo University'),
    ('19', 'Stony Brook University'),
    ('20', 'University of Ottawa'),
    ('21', 'Berea College'),
    ('22', 'Massasoit CC'),
    ('23', 'University of Massachusetts'),
    ('24', 'University of South Florida'),
    ('25', 'Princeton University'),
    ('26', 'Montclair State University'),
    ('27', 'University of Georgia'),
    ('28', '------------------------'),
)

# User model
class User(AbstractUser):
    RANK_CHOICES = (
        ('A', 'mentor'),
        ('B', 'mentee'),
    )

    rank = models.CharField(max_length=255, choices=RANK_CHOICES, default=RANK_CHOICES[1], null=True,)
    undergrad_college = models.CharField(max_length=255, choices=UNIVERSITIES, default='No University')
    hidden = models.BooleanField(default = False)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return "%s" % self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def get_university(self):
        "get the mentors university"
        return self.university

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

User._meta.get_field('email')._unique = True


#class Mentee(models.Model):
#    user        = models.OneToOneField(User)
#    picture     = models.ImageField(upload_to="profile_images", blank=True)
#    #graduating = models.DateField() OR highschool = models.CharField(max_lenght=255, choices=HIGHSCHOOLS, required=True)

#    def __str__(self):
#      return "mentee's profile %s" % self.user.email


# Mentor model
class Mentor(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to="mentor_profile_images", blank=True)
    biography = models.TextField(null=True)
#    graduating  = models.DateField()
    undergrad_college = models.CharField(max_length=255, choices=UNIVERSITIES, default='No University', help_text='Your Undergraduate College')
    grad_college = models.CharField(max_length=255, choices=UNIVERSITIES, default='No University', help_text='Your Graduate College')
    majors = models.CharField(max_length=100)
    interests = models.CharField(max_length=150)
    residency = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, default='+(000)0000000')
    current_status = models.CharField(max_length=255)
    school_haiti = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
#   mentees = models.ManyToManyField(Mentee)
#   todos = models.ManyToManyField(ToDo)
    hidden = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["university"]

    def __str__(self):
        return "mentor's profile %s" % self.user.email


# To-do App. user is a Mentor, has an emission date, has an expiration date, has a subject.
class ToDo(models.Model):
    author = models.CharField(max_length=25, default='New Author')
    subject = models.CharField(max_length=200)
    emitted = models.DateField(auto_now_add=True)
    expires = models.DateField()
    completion = models.BooleanField(default=False)

    def __str__(self):
        return self.subject + 'by' + self.Mentor.user.name

    def auto_delete(self):
        today = datetime.now().date
        if self.expires == today:
            self.delete()
