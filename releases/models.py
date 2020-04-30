import uuid

from django.db import models
from model_utils.models import TimeStampedModel

from projects.models import Project


class Release(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    tag = models.CharField(max_length=100)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    attachment = models.FileField()


class ReleaseObservation(TimeStampedModel):
    stakeholder_email = models.EmailField()
    release = models.ForeignKey(Release, on_delete=models.PROTECT)
    score = models.CharField(max_length=100, null=True, blank=True)  # choices
    comment = models.CharField(max_length=2000, null=True, blank=True)
    email_status = models.CharField(max_length=2000, null=True, blank=True)  # Webhook callback for postback
