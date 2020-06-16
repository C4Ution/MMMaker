from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    STATUS_0, STATUS_1, STATUS_2, STATUS_3, STATUS_4 = 0, 10, 20, 30, 40
    STATUS_TYPE = (
        (STATUS_0, '0'),
        (STATUS_1, '10'),
        (STATUS_2, '20'),
        (STATUS_3, '30'),
        (STATUS_4, '40'),
    )
    status = models.IntegerField(choices=STATUS_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskResource(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_resource')
    url = models.URLField(max_length=200)
