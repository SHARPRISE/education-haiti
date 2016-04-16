from django.conf.urls import patterns, url, include
from datetime import datetime

from . import views

urlpatterns = [
    url(r'^our_mentors$', views.our_mentors, name='our_mentors'),
]