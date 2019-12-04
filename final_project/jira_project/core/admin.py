from django.contrib import admin
from .models import Task, TaskDocument, Project, ProjectMember

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', )
admin.site.register(TaskDocument)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'user')
