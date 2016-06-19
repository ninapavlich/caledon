import datetime

from django.db import models
from django.db.models import Q, get_model
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError 
from django.core.urlresolvers import reverse
from django.db.utils import DatabaseError
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _


from carbon.utils.slugify import unique_slugify


class BaseModel(models.Model):

    created_date    = models.DateTimeField(auto_now_add=True)

    def get_edit_url(self):
        return reverse('admin:%s_%s_change' %(self._meta.app_label,  self._meta.model_name),  args=[self.id] )

    def get_edit_link(self):
        return '<a href="%s" target="_blank">Edit &rarr;</a>'%(self.get_edit_url())
    get_edit_link.allow_tags = True

    class Meta:
        abstract = True          

class Match(BaseModel):
    title   = models.CharField( max_length = 255)
    slug    = models.CharField( max_length = 255)

    def __unicode__(self):
        return "MATCH %s" % ( self.title )

    def get_absolute_url(self):
        return reverse('match_detail_view',  args=[self.slug] )

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
        ordering = [ '-created_date' ] 

    def save(self, *args, **kwargs):
        unique_slugify(self, self.title) 
        super(Match, self).save(*args, **kwargs)


class MatchUser(BaseModel):
    match = models.ForeignKey('celadon.Match')
    user = models.ForeignKey('account.User')




    class Meta:
        ordering = [ '-created_date' ] 


class MatchLogs(BaseModel):
    match = models.ForeignKey('celadon.Match')
    user = models.ForeignKey('account.User')

    class Meta:
        verbose_name = "Match Log"
        verbose_name_plural = "Match Logs"
        ordering = [ '-created_date' ] 
    #TODO -- add details


