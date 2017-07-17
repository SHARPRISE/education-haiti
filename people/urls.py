from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from datetime import datetime

from . import views

urlpatterns = [
    #url(r'^login/$', views.login_view, name='login'),
    #url(r'^register/$', views.register, name='register'),
]

#CREATE UNIQUE INDEX people_todo_author_id_key ON people_todo USING BTREE (author_id);
