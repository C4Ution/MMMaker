from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View


class CreateTaskView(View):
    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()


        return JsonResponse({})


class CheckTaskStatusView(View):
    def get(self, request, *args, **kwargs):
        if not request.is_ajax:
            return HttpResponseBadRequest()
        return JsonResponse({})
