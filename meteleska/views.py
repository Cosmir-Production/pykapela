
from django.shortcuts import render

from meteleska.base.views import BaseView
from meteleska.events.models import Event


class WebView(BaseView):

    @staticmethod
    def index(request, context):

        context['events'] = Event.objects.filter(
            is_published=True,
        )

        return render(request, 'index.html', context)
