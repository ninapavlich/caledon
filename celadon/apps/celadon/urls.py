from django.conf.urls import patterns, url, include

from .views import *

urlpatterns = patterns('',
    
    url(r'^(?P<slug>[\w-]+)/$', MatchView.as_view(), name="match_view"),

)