from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from projects.models import Project
from releases.models import Release, ReleaseObservation


class PostmarkWebhook(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, project_slug, **kwargs):
        project = Project.objects.get(slug=project_slug)
        last_release = project.release_set.last()
        # TODO Get email and type of webhook
        body = request.body.decode('utf-8')
        return JsonResponse({'status': 'ok'})


class FeedbackView(TemplateView):
    template_name = 'feedback.html'

    def get(self, request, release, email, **kwargs):
        get_object_or_404(Release, uuid=release)
        return super().get(request, release, email, **kwargs)

    def post(self, request, release, email, **kwargs):
        release_instance = get_object_or_404(Release, uuid=release)
        self.update_observation(request, release_instance, email)
        messages.success(request, 'Feedback enviado, muchas gracias')
        return redirect('feedback', release=release, email=email)

    def update_observation(self, request, release, email):
        score = request.POST.get('score')
        comment = request.POST.get('comment')
        observation = release.releaseobservation_set.filter(
            stakeholder_email=email
        ).first()

        if not observation:
            ReleaseObservation.objects.create(
                release=release,
                stakeholder_email=email,
                score=score,
                comment=comment)
        else:
            observation.comment = comment
            observation.score = score
            observation.save()


class SendReleaseView(View):
    def get(self, request, release_id, **kwargs):
        release = Release.objects.select_related('project').get(pk=release_id)
        project = release.project

        email = EmailMessage(
            subject=release.subject,
            message=release.body,
            html_message=release.body,
            from_email=project.from_email,
            to=project.team_mails + project.stakeholder_emails,
            fail_silently=False
        )
        email.content_subtype = 'html'
        if release.attachment:
            email.attach_file(release.attachment.path)
        email.send()
