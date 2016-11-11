
from django.shortcuts import render
from django.utils import timezone

from project.base.views import BaseView
from project.events.models import Event


class WebView(BaseView):

    @staticmethod
    def index(request, context):

        # concert stay on homepage till this midnight
        context['events'] = Event.objects.filter(
            is_published=True,
            datetime__gte=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        )
        context['events_count'] = context['events'].count()

        return render(request, 'index.html', context)
