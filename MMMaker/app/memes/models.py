from django.db import models
from django.conf import settings


class Task(models.Model):
    STATUS_QUEUED, STATUS_STARTED, STATUS_DOWNLOAD, STATUS_EXTRACT_HIGHLIGHT, STATUS_ADJUST_SOUNDS, STATUS_APPLY_EFFECTS, STATUS_MERGE_VIDEOS, STATUS_UPLOADER, STATUS_COMPLETE, STATUS_FAILED = 20, 30, 40, 50, 60, 70, 80, 90, 100, 0

    STATUS_CHOICES = (
        (STATUS_QUEUED, 'Queueing on server...'),
        (STATUS_STARTED, 'Starting to edit...'),
        (STATUS_DOWNLOAD, 'Downloading resources...'),
        (STATUS_EXTRACT_HIGHLIGHT, 'Extracting highlights...'),
        (STATUS_ADJUST_SOUNDS, 'Adjusting pitches...'),
        (STATUS_APPLY_EFFECTS, 'Applying video effects...'),
        (STATUS_MERGE_VIDEOS, 'Merging video clips...'),
        (STATUS_UPLOADER, 'Uploading videos...'),
        (STATUS_COMPLETE, 'All done!'),
        (STATUS_FAILED, 'Error occurred'),
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
