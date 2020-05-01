from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from tinymce.widgets import TinyMCE

from .models import Release, ReleaseObservation


class ReleaseObservationInline(admin.TabularInline):
    model = ReleaseObservation
    extra = 0
    readonly_fields = ('delivered_at', 'openned_at', 'clicked_at')


class ReleaseAdmin(admin.ModelAdmin):
    inlines = (ReleaseObservationInline, )
    list_display = ('project', 'tag', 'uuid', 'send_url')
    list_filter = ('project', )
    date_hierarchy = 'created'
    readonly_fields = ('sent', )

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'body': TinyMCE
        }
        return super().get_form(request, obj, **kwargs)

    def send_url(self, obj):
        url = reverse('send_release', kwargs=dict(release_id=obj.id))
        return format_html(f'<a href="{url}">Send</a>')
    send_url.short_description = 'Send email'


admin.site.register(Release, ReleaseAdmin)
