
from django.shortcuts import render

from meteleska.base.views import BaseView


class WebView(BaseView):

    def __init__(self, **kwargs):
        super(WebView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):

        context = self._prepare_context()

        view = getattr(self, request.resolver_match.view_name, None)
        return view(request, context, *args, **kwargs)

    @staticmethod
    def index(request, context):

        return render(request, 'index.html', context)
