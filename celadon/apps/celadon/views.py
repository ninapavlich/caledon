from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import HttpResponse, Http404, HttpResponseServerError
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import ListView, DetailView

from carbon.atoms.views.abstract import *
from carbon.atoms.views.content import *

from .models import *



class MatchDetailView(ObjectTemplateResponseMixin, DetailView): #TODO -- move templates to ObjectTemplateResponseMixin, SingleObjectMixin, 
    template_name="caledon/match_detail.html"
    model = Match
    slug_field = 'matchid'
    slug_url_kwarg = 'id'

    def get_template_names(self):
        return ['celadon-match']

    def get_template(self):
        return self.object.template


class MatchListView(ObjectTemplateResponseMixin, ListView): #TODO -- move templates to ObjectTemplateResponseMixin, SingleObjectMixin, 
    template_name="caledon/match_list.html"
    model = Match
    paginate_by = 10

    def get_template_names(self):
        return ['celadon-matches']
