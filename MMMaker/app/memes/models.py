from django.db import models


class Task(models.Model):
    STATUS_QUEUED, STATUS_STARTED, STATUS_DOWNLOAD, STATUS_FAILED = 10, 20, 30, 0
    STATUS_CHOICES = (
        (STATUS_QUEUED, '서버 작업 대기중'),
        (STATUS_STARTED, '서버 작업 시작'),
        (STATUS_DOWNLOAD, '서버 리소스 다운로드'),
        (STATUS_FAILED, '작업 실패'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_QUEUED)
    created = models.DateTimeField(auto_now_add=True)
    result_url = models.URLField(null=True)

    def __str__(self):
        return 'task#{}'.format(self.id)


class TaskResource(models.Model):
    task = models.ForeignKey('memes.Task', on_delete=models.CASCADE, related_name='task_resources')
    url = models.URLField()
