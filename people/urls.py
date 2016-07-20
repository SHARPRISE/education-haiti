from django.conf.urls import patterns, url, include
from datetime import datetime

from . import views

urlpatterns = [
    #url(r'^login/$', views.login_view, name='login'),
    url(r'^mentor_login/$', views.mentor_login, name='mentor_login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    #url(r'^register/$', views.register, name='register'),
    url(r'^mentor_update/$', views.mentor_update, name='mentor_update'),
    #url(r'^mentor_register/$', views.register_mentor, name='mentor_register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^mentor_profile/$', views.mentor_profile, name='mentor_profile'),
    url(r'^add_story_form/$', views.add_story, name='add_story_form'),
    url(r'^new_story/$', views.new_story, name='new_story')
]
