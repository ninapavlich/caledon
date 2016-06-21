from django.conf.urls import patterns, url, include

from .views import *

urlpatterns = patterns('',
    
    url(r'^matches/(?P<id>[\w-]+)/$', MatchDetailView.as_view(), name="match_detail_view"),
    url(r'^matches/$', MatchListView.as_view(), name="match_list_view"),

)