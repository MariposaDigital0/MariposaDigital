from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from mariposa.task.models import Task


class Board(models.Model):
    b_name = models.CharField(max_length=45)
    sequence = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.b_name


class TaskOnBoard(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    sequence = models.IntegerField()
