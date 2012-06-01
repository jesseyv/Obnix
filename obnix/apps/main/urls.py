# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from obnix.apps.main.views import IndexPageView

urlpatterns = patterns('',
    url(r'^$', IndexPageView.as_view(),
        name='index',
    ),
)