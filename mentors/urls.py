from django.conf.urls import url, include
from datetime import datetime

from . import views

urlpatterns = [
    url(r'^$', views.mentors, name='our_mentors'),
    url(r'^mentor_application/$', views.become_a_mentor, name='mentor_application')
]
