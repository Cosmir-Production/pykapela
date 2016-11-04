
from django.shortcuts import render

from project.base.views import BaseView
from project.events.models import Event


class WebView(BaseView):

    @staticmethod
    def index(request, context):

        context['events'] = Event.objects.filter(
            is_published=True,
        )

        return render(request, 'index.html', context)
