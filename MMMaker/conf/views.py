from django.views.generic import TemplateView
from misc import random_str

import json


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['randoms'] = json.dumps([random_str() for _ in range(5)])
        return context
