from django.conf.urls import patterns, include, url
from django.contrib import admin

import zizouCounter

urlpatterns = patterns(
  '',
  url(r'^', include('zizouCounter.urls')),
)
