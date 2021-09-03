from django.db import models
from django.db.models.base import Model
from mariposa.user.models import CustomUser


class Project(models.Model):
    p_name = models.CharField(max_length=100)
    description = models.TextField()
    planned_start_date = models.DateField(auto_now=False, auto_now_add=False)
    planned_end_date = models.DateField(auto_now=False, auto_now_add=False)
    actual_start_date = models.DateField(auto_now=False, auto_now_add=False)
    actual_end_date = models.DateField(auto_now=False, auto_now_add=False)
    estimated_hours = models.CharField(max_length=45)
    actual_hours = models.CharField(max_length=45)
    estimated_budget = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE)
    project_no = models.CharField(max_length=45)
    projectcol = models.CharField(max_length=45)

    def __str__(self):
        return self.p_name


class ProjectManager(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_account_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class ClientPartner(models.Model):
    cp_name = models.CharField(max_length=45)
    cp_address = models.CharField(max_length=45)
    cp_details = models.CharField(max_length=45)
    user_account_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.cp_name


class OnProject(models.Model):
    cp_id = models.ForeignKey(ClientPartner, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    is_partner = models.BooleanField()
    is_client = models.BooleanField()
