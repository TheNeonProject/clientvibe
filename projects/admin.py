from django.contrib import admin
from django import forms

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'team_emails': forms.Textarea,
            'stakeholder_emails': forms.Textarea
        }
        return super().get_form(request, obj, **kwargs)


admin.site.register(Project, ProjectAdmin)
