from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model

User = get_user_model()


class Requirments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    req = models.FileField(upload_to='req/docs/')


class Jobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    j_title = models.CharField(max_length=100)
    desc = models.TextField()
    TODO = 'TD'
    DOING = 'DG'
    DONE = 'DN'
    STATE = [
        (TODO, 'Todo'),
        (DOING, 'Doing'),
        (DONE, 'Done'),
    ]
    state = models.CharField(
        max_length=2,
        choices=STATE,
        default=TODO,
    )

    def __str__(self):
        return self.j_title
