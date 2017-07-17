from django.conf.urls import url, include
from datetime import datetime

from . import views

urlpatterns = [
    url(r'^$', views.programs, name='programs'),
]
