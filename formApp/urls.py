# -*- coding: utf-8 -*-
# __author__ = "belic"
# __datetime__ = "2018/5/27 11:28"
from django.conf.urls import url
from django.urls import path, include, re_path

from .views import FormAppTestView

app_name = "form_app"

urlpatterns = [
    re_path('^register/$', FormAppTestView.as_view())
]