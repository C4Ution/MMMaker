from django.contrib import admin
from .models import Task, TaskResource


# Register your models here.
admin.site.register(Task)
admin.site.register(TaskResource)
