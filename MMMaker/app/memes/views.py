from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.db import transaction
from django.shortcuts import get_object_or_404

from app.memes.models import Task, TaskResource
from tasks.task import make_meme


class CreateTaskView(View):
    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        files = request.POST.getlist('file[]')
        if not files:
            return HttpResponseBadRequest()

        with transaction.atomic():
            task = Task.objects.create()
            task_resources = []
            for file in files:
                task_resources.append(
                    TaskResource(task=task, access_key=file)
                )
            TaskResource.objects.bulk_create(task_resources)
        make_meme.delay(task.id)
        return JsonResponse({
            'id': task.id,
            'msg': task.get_status_display(),
            'status': task.status,
        })


class CheckTaskStatusView(View):
    def get(self, request, *args, **kwargs):
        if not request.is_ajax:
            return HttpResponseBadRequest()

        task = get_object_or_404(Task, id=kwargs.get('pk'))
        ret = {
            'msg': task.get_status_display(),
            'status': task.status,
        }
        if task.result_url:
            ret['result_url'] = task.result_url
        return JsonResponse(ret)
