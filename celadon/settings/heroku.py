from celadon.settings.base import *
import dj_database_url
import herokuify

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = env.get("DEBUG", False)
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']



DATABASES['default'] =  dj_database_url.config()

CACHES = herokuify.get_cache_config()   # Memcache config for Memcache/MemCachier
CACHES['dbtemplates'] = CACHES['default']