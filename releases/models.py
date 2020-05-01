import uuid

from django.db import models
from model_utils.models import TimeStampedModel

from projects.models import Project


class Release(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    tag = models.CharField(max_length=100)
    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    attachment = models.FileField(null=True, blank=True)
    sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.tag


class ReleaseObservation(TimeStampedModel):
    OPEN = 'Open'
    DELIVERY = 'Delivery'
    CLICK = 'Click'
    EMAIL_STATUS = [
        (OPEN, OPEN),
        (DELIVERY, DELIVERY),
        (CLICK, CLICK)
    ]

    stakeholder_email = models.EmailField()
    release = models.ForeignKey(Release, on_delete=models.PROTECT)
    score = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=2000, null=True, blank=True)
    email_status = models.CharField(
        choices=EMAIL_STATUS,
        max_length=2000, null=True, blank=True
    )
    delivered_at = models.DateTimeField(null=True, blank=True, editable=False)
    openned_at = models.DateTimeField(null=True, blank=True, editable=False)
    clicked_at = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.stakeholder_email
