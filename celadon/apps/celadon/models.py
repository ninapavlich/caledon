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


class BaseModel(models.Model):

    created_date    = models.DateTimeField(auto_now_add=True)
    
    def get_edit_url(self):
        return reverse('admin:%s_%s_change' %(self._meta.app_label,  self._meta.model_name),  args=[self.id] )

    def get_edit_link(self):
        return '<a href="%s" target="_blank">Edit &rarr;</a>'%(self.get_edit_url())
    get_edit_link.allow_tags = True

    class Meta:
        abstract = True          

class Config(BaseModel):
    """
    Django model for settings, to allows configuring kiosk variables through
    the admin interface.
    """
    TYPE_CHOICES = (
        ('string', 'String'),
        ('int', 'Integer'),
        ('decimal', 'Decimal'),
        ('bool', 'Boolean'),
    )
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField(blank=False)
    value_type = models.CharField(max_length=200, blank=False,
                                  choices=TYPE_CHOICES)
    help = models.TextField( help_text = "Additional information about this value.", null = True )

    # -- PROPERTIES -- #
    # -- INSTANCE METHODS -- #    
    def typed_js( self ):
        """
        Value Formatted for Javascript
        """
        if self.value_type in [ 'bool', 'int', 'decimal' ]:
            return self.value
        elif self.value_type == 'string':
            return '"%s"' % self.value
    
    def __unicode__(self):
        return "%s:%s" % ( self.key, self.value )

    # -- STATIC AND CLASS METHODS -- #
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "key__icontains", "value__icontains")

    class Meta:
        verbose_name = "Generic Configuration Value"
        verbose_name_plural = "Generic Configuration Values"
        ordering = [ 'key' ]

