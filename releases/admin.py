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
    list_display = ('project', 'tag', 'uuid', 'send_url', 'sent')
    list_filter = ('project', )
    date_hierarchy = 'created'
    readonly_fields = ('sent', )
    fieldsets = [
        ('Default', {
            'fields': (
                'project', 'tag', 'subject', 'body', 'attachment'
            ),
            'description': '''
                <h1>IMPORTANT! You need to set a webhook on postmark per project.</h1>

                <p>
                   In order to get the email status information from the stakeholders, you need to
                   set a Webhook on Postmark with the following url pattern: <strong>https://clientvi.be/postmark/</strong>
                </p>

                <p>
                   To select the project you need to set a Header for the webhook <strong>slug: *project_slug*</strong>
                </p>

                <p>You need to check <strong>Delivery</strong>, <strong>Open</strong> and <strong>Click</strong></p>

                <p>To set a webhook you need to go to your Server in Postmark -> Default Transactional Streams -> Webhook</p>
            '''
        })]

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'body': TinyMCE
        }
        return super().get_form(request, obj, **kwargs)

    def send_url(self, obj):
        if obj.sent:
            return '<strong>Already sent</strong>'

        url = reverse('send_release', kwargs=dict(release_id=obj.id))
        return format_html(f'<a href="{url}">Send</a>')
    send_url.short_description = 'Send email'


admin.site.register(Release, ReleaseAdmin)
