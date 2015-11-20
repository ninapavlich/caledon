from django.db import models
from django.conf import settings

from carbon.atoms.models.abstract import VersionableAtom, TitleAtom, OrderedItemAtom, HierarchicalAtom
from carbon.compounds.page.models import Page as BasePage
from carbon.compounds.page.models import PageContentBlock as BasePageContentBlock

    
class Page(BasePage):
    default_template = 'page_base'


    def get_page_content_blocks(self):
        blocks = PageContentBlock.objects.filter(parent=self).order_by('order')
        published = [block for block in blocks if block.is_published()]
        return published


class PageContentBlock(BasePageContentBlock):
    pass

class PageSlide(VersionableAtom, OrderedItemAtom):
    
    parent = models.ForeignKey('page.Page')

    slide_image = models.ForeignKey('media.Image', null=True, blank=True)

    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['order']
