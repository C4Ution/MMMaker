import os

from celery import Celery
from django.conf import settings


CELERY_IMPORTS = (
    'tasks.task',
)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
app = Celery('conf', broker=settings.BROKER_URL, include=CELERY_IMPORTS)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
