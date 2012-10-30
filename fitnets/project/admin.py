from django.contrib import admin
from models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('objective', 'creator', 'created')
    exclude = ('creator', 'created', 'updater', 'updated')

admin.site.register(Project, ProjectAdmin)