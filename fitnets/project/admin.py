from django.contrib import admin
from models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('objective', 'creator', 'created')
    exclude = ('creator', 'created', 'updater', 'updated')

class CommentProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project')
    list_filters = ('project', )

class TrainingDayAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created', 'updater', 'updated')
    list_display = ('__unicode__', 'day')

class TrainingExerciseAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created', 'updater', 'updated')
    list_display = ('__unicode__', 'exercise')

admin.site.register(Project, ProjectAdmin)
admin.site.register(CommentProject, CommentProjectAdmin)
admin.site.register(TrainingExercise, TrainingExerciseAdmin)
admin.site.register(TrainingDay, TrainingDayAdmin)