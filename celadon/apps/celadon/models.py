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
    #title          = models.CharField( max_length = 255)
    #slug           = models.CharField( max_length = 255)
    matchid        = models.CharField( max_length = 255)
    date           = models.CharField( max_length = 255) #not using DateTimeField because this will be written to by a Java server, which doesn't know how to create a Python Date object
    mapname        = models.CharField( max_length = 255)
    winningteam    = models.CharField( max_length = 255, null=True)
    match_complete = models.BooleanField( )
    match_aborted  = models.BooleanField( )
    
    def __unicode__(self):
       return "MATCH %s - %s" % ( self.matchid, self.mapname )

    def get_absolute_url(self):
       return reverse('match_detail_view',  args=[self.matchid] )

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
        ordering = [ '-created_date' ] 

    #def save(self, *args, **kwargs):
    #    unique_slugify(self, self.title) 
    #    super(Match, self).save(*args, **kwargs)


class MatchUser(BaseModel):
    match = models.ForeignKey('celadon.Match')
    user  = models.ForeignKey('celadon.Player')
    role  = models.CharField( max_length = 255)

    class Meta:
        ordering = [ '-created_date' ] 

class Player(BaseModel):
    
    uuid          = models.CharField( max_length = 255 )
    bio           = models.TextField( null=True )
    current_match = models.ForeignKey('celadon.Match', null=True)

    class Meta:
        ordering = [ '-created_date' ]     
        
class MatchLogs(BaseModel):
    match           = models.ForeignKey('celadon.Match')
    timestamp       = models.CharField(max_length = 255)
    player          = models.ForeignKey('celadon.Player', null=True)
    affected_player = models.ForeignKey('celadon.Player', related_name='player', null=True)
    logmessage      = models.CharField(max_length = 255)
    logtype         = models.ForeignKey('celadon.LogType')
    
    class Meta:
        verbose_name = "Match Log"
        verbose_name_plural = "Match Logs"
        ordering = [ '-created_date' ] 
    #TODO -- add details

class LogType(BaseModel):
    typeid      = models.CharField( max_length = 255)
    description = models.CharField( max_length = 255)
    
    class Meta:
        verbose_name = "Log Type"
        verbose_name_plural = "Log Types"
        ordering = [ '-created_date' ] 
    