from django.contrib import admin
from models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('objective', 'creator', 'created')
    exclude = ('creator', 'created', 'updater', 'updated')

class CommentProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project')
    list_filters = ('project', )

admin.site.register(Project, ProjectAdmin)
admin.site.register(CommentProject, CommentProjectAdmin)