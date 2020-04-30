from django.contrib import admin
from django import forms

from .models import Release, ReleaseObservation


class ReleaseObservationInline(admin.TabularInline):
    model = ReleaseObservation
    extra = 0


class ReleaseAdmin(admin.ModelAdmin):
    inlines = (ReleaseObservationInline, )

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'body': forms.Textarea
        }
        return super().get_form(request, obj, **kwargs)


admin.site.register(Release, ReleaseAdmin)
