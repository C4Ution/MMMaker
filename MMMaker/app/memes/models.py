from django.db import models
from django.conf import settings


class Task(models.Model):
    STATUS_QUEUED, STATUS_STARTED, STATUS_DOWNLOAD, STATUS_EXTRACT_HIGHLIGHT, STATUS_ADJUST_SOUNDS, STATUS_APPLY_EFFECTS, \
    STATUS_MERGE_VIDEOS, STATUS_UPLOADER, STATUS_COMPLETE, STATUS_FAILED = 10, 20, 30, 40, 50, 60, 70, 80, 90, 0

    STATUS_CHOICES = (
        (STATUS_QUEUED, '서버 작업 대기중'),
        (STATUS_STARTED, '서버 작업 시작'),
        (STATUS_DOWNLOAD, '서버 리소스 다운로드'),
        (STATUS_EXTRACT_HIGHLIGHT, '영상 하이라이트 추출'),
        (STATUS_ADJUST_SOUNDS, '음계 조정'),
        (STATUS_APPLY_EFFECTS, '영상 효과 추가'),
        (STATUS_MERGE_VIDEOS, '영상 합성'),
        (STATUS_UPLOADER, '영상 업로드'),
        (STATUS_COMPLETE, '업로드 완료'),
        (STATUS_FAILED, '작업 실패'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_QUEUED)
    created = models.DateTimeField(auto_now_add=True)
    result_url = models.URLField(null=True)

    def __str__(self):
        return 'task#{}'.format(self.id)


class TaskResource(models.Model):
    task = models.ForeignKey('memes.Task', on_delete=models.CASCADE, related_name='task_resources')
    access_key = models.CharField(max_length=100)

    @property
    def file_url(self):
        return settings.CUSTOM_DOMAIN.format(self.access_key)
