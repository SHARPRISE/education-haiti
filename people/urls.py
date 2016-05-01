from django.conf.urls import patterns, url, include
from datetime import datetime

from . import views

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^mentor_login/$', views.mentor_login, name='mentor_login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^mentor_register/$', views.register_mentor, name='mentor_register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]
