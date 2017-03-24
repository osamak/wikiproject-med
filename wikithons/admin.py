from django.contrib import admin
from .models import Location, Wikithon, Team

class LocationAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ['name', 'long_position', 'lat_position']

class WikithonAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ['name', 'date', 'submission_date']

class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ['name', 'wikithon', 'get_founder_name',
                    'get_member_count', 'submission_date']
    list_filter = ['wikithon']

    def get_founder_name(self, obj):
        if obj.founder:
            return obj.founder.profile.name


admin.site.register(Location, LocationAdmin)
admin.site.register(Wikithon, WikithonAdmin)
admin.site.register(Team, TeamAdmin)
