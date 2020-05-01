from django.db import models

from model_utils.models import TimeStampedModel


class Project(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    from_email = models.CharField(max_length=100)
    team_emails = models.CharField(max_length=500)
    stakeholder_emails = models.CharField(max_length=500)

    def __str__(self):
        return self.name
