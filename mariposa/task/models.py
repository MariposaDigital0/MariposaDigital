from django.db import models
from django.db.models.base import Model
from mariposa.project.models import Project, ClientPartner
from mariposa.user.models import Employee, Role


class Task(models.Model):
    t_name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    planned_start_date = models.DateField(auto_now=False, auto_now_add=False)
    planned_end_date = models.DateField(auto_now=False, auto_now_add=False)
    actual_start_date = models.DateField(auto_now=False, auto_now_add=False)
    actual_end_date = models.DateField(auto_now=False, auto_now_add=False)
    estimated_hours = models.CharField(max_length=45)
    actual_hours = models.CharField(max_length=45)
    estimated_budget = models.CharField(max_length=45)
    actual_budget = models.CharField(max_length=45)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_adhoc = models.BooleanField()
    client_partner_id = models.ForeignKey(
        ClientPartner, on_delete=models.CASCADE)

    def __str__(self):
        return self.t_name


class Assigned(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
