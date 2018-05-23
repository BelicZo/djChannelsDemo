# -*- coding: utf-8 -*-
# __author__ = "belic"
# __datetime__ = "2018/5/23 21:46"
from django.urls import re_path, path

from . import views

app_name = "chat"

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
