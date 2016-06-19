from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from carbon.utils.admin.actions import output_csv
from carbon.utils.admin.actions import resave_item

from celadon.apps.page.sitemap import *


admin.autodiscover()
admin.site.add_action(output_csv)
admin.site.add_action(resave_item)

sitemaps = {
    'pages': PageSitemap
}


urlpatterns = patterns('')


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls))
    )

SERVE_STATIC_FILES = settings.IS_ON_HEROKU or not settings.IS_ON_SERVER
if SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        (r'', include('carbon.urls_favicons')),
    )

    if settings.STATIC_ROOT:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





urlpatterns +=  patterns('',
    
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^robots\.txt$', include('robots.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    (r'^', include('carbon.compounds.core.urls')),    

    (r'^', include('carbon.utils.admin.urls')),    
  

    # -- celadon URLS
    

    url(r'^', include('celadon.apps.media.urls')),
    url(r'^', include('celadon.apps.form.urls')),
    url(r'^', include('celadon.apps.email.urls')),
    url(r'^', include('celadon.apps.celadon.urls')),
    url(r'^', include('celadon.apps.page.urls')),
    
)





