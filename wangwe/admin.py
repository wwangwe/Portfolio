from django.contrib import admin
from .models import Feedback, Project


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Feedback, FeedbackAdmin)