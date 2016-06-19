from django.contrib import admin

from django_unsaved_changes.admin import UnsavedChangesAdmin

from .models import *



class MatchUserInline(admin.TabularInline):
    model = MatchUser
    extra = 0
   
    autocomplete_lookup_fields = {
        'fk': ['user'],
    }
    raw_id_fields = ('user', ) 

class MatchAdmin(UnsavedChangesAdmin):

    prepopulated_fields = {"slug": ("title",)}
    inlines = [MatchUserInline]


class MatchUserAdmin(UnsavedChangesAdmin):

    autocomplete_lookup_fields = {
        'fk': ['match', 'user'],
    }
    raw_id_fields = ('match', 'user', ) 


class MatchLogsAdmin(UnsavedChangesAdmin):

    autocomplete_lookup_fields = {
        'fk': ['match', 'user'],
    }
    raw_id_fields = ('match', 'user', ) 



admin.site.register(Match, MatchAdmin)
admin.site.register(MatchUser, MatchUserAdmin)
admin.site.register(MatchLogs, MatchLogsAdmin)