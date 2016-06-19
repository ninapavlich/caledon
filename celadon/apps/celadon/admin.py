from django.contrib import admin

from django_unsaved_changes.admin import UnsavedChangesAdmin

from .models import *



class MatchAdmin(UnsavedChangesAdmin):
    
    pass


class MatchUserAdmin(UnsavedChangesAdmin):

    pass


class MatchLogsAdmin(UnsavedChangesAdmin):

    pass



admin.site.register(Match, MatchAdmin)
admin.site.register(MatchUser, MatchUserAdmin)
admin.site.register(MatchLogs, MatchLogsAdmin)