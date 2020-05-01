from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE

from .models import Release, ReleaseObservation


class ReleaseObservationInline(admin.TabularInline):
    model = ReleaseObservation
    extra = 0
    readonly_fields = ('delivered_at', 'openned_at', 'clicked_at')


class ReleaseAdmin(admin.ModelAdmin):
    inlines = (ReleaseObservationInline, )
    list_display = ('project', 'tag', 'uuid', 'send')
    list_filter = ('project', )
    date_hierarchy = 'created'
    readonly_fields = ('sent', )

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'body': TinyMCE
        }
        return super().get_form(request, obj, **kwargs)

    def send(self, obj):
        return f'<a href="/send/{obj.id}/">Send</a>'
    send.allow_tags = True


admin.site.register(Release, ReleaseAdmin)
