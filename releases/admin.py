from django.contrib import admin
from django import forms

from .models import Release, ReleaseObservation


class ReleaseObservationInline(admin.TabularInline):
    model = ReleaseObservation
    extra = 0


class ReleaseAdmin(admin.ModelAdmin):
    inlines = (ReleaseObservationInline, )
    list_display = ('project', 'tag', 'send')
    list_filter = ('project', )
    date_hierarchy = 'created'
    readonly_fields = ('sent', )

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'body': forms.Textarea
        }
        return super().get_form(request, obj, **kwargs)

    def send(self, obj):
        # TODO
        return 'Send'


admin.site.register(Release, ReleaseAdmin)
