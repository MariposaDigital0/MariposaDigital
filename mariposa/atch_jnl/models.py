from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from mariposa.task.models import Task
from mariposa.project.models import Project


class Attachments(models.Model):
    project_id = models.ForeignKey(Project, on_delete=CASCADE)
    media = models.FileField(null=True, blank=True)
    task_id = models.ForeignKey(Task, on_delete=CASCADE)
