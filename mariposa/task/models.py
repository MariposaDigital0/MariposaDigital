from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F
from mariposa.project.models import Project, ClientPartner
from mariposa.user.models import Employee, Role


class Task(models.Model):
    t_name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    planned_start_date = models.DateField(auto_now=False, auto_now_add=False)
    planned_end_date = models.DateField(auto_now=False, auto_now_add=False)
    actual_start_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    actual_end_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    estimated_hours = models.CharField(max_length=45)
    actual_hours = models.CharField(max_length=45, null=True, blank=True)
    estimated_budget = models.CharField(max_length=45)
    actual_budget = models.CharField(max_length=45, null=True, blank=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_adhoc = models.BooleanField(default=False)
    client_partner_id = models.ForeignKey(
        ClientPartner, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.t_name


class Assigned(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
