# -*- coding: utf-8 -*-
# __author__ = "belic"
# __datetime__ = "2018/5/23 21:53"
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.MyConsumer),
]