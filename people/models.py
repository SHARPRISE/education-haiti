from django.db import models
from django.contrib.auth.models import AbstractUser

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


# HIGHSCHOOLS = ()


#class Mentee(models.Model):
 #   user        = models.OneToOneField(User)
 #   picture     = models.ImageField(upload_to="profile_images", blank=True)
 #   #graduating = models.DateField() OR highschool = models.CharField(max_lenght=255, choices=HIGHSCHOOLS, required=True)

  #  def __str__(self):
  #      return "mentee's profile %s" % self.user.email

# Mentor model
class Mentor(models.Model):
    user        = models.OneToOneField(User)
    picture     = models.ImageField(upload_to="mentor_profile_images", blank=True)
    biography   = models.TextField(null=True)
    #graduating  = models.DateField()
    undergrad_college = models.CharField(max_length=255, choices=UNIVERSITIES, default='No University')
    grad_college = models.CharField(max_length=255, choices=UNIVERSITIES, default='No University')
    majors = models.CharField(max_length=100, default='Your major(s), please separate each major with a comma')
    interests = models.CharField(max_length=150, default='Your interests, please separate each one with a comma')
    residency = models.CharField(max_length=255, default='Your state/city of residency')
    phone = models.CharField(max_length=255, default='Your phone number')
    current_status = models.CharField(max_length=255, default='Your current status/work')
    school_haiti = models.CharField(max_length=255, default='Your school in Haiti')
    first_name = models.CharField(max_length=100, default='Your first name')
    last_name = models.CharField(max_length=100, default='Your last name')
    #mentees     = models.ManyToManyField(Mentee)
    hidden      = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["university"]

    def __str__(self):
        return "mentor's profile %s" % self.user.email
