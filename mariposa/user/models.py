from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    session_token = models.CharField(max_length=10, default=0)
    is_project_manager = models.BooleanField(default=False)
    ADMIN = 'MG'
    DEVELOPER = 'DV'
    CLIENT = 'CL'
    TESTER = 'QA'
    STATE = [
        (ADMIN, 'Admin'),
        (DEVELOPER, 'Developer'),
        (CLIENT, 'client'),
        (TESTER, 'tester'),
    ]
    u_type = models.CharField(
        max_length=2,
        choices=STATE,
        default=ADMIN,
    )


class Employee(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    user_account_id = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Team(models.Model):
    t_name = models.CharField(max_length=45)

    def __str__(self):
        return self.t_name


class Role(models.Model):
    r_name = models.CharField(max_length=45)

    def __str__(self):
        return self.r_name


class TeamMember(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
