from django.shortcuts import render

from project.base.views import BaseView
from project.events.models import Event
from project.social.models import Social


class EventView(BaseView):

    """
    Homepage
    """
    @staticmethod
    # @cache_page(settings.CACHE_VIEWS_DEFAULT_TIME)
    def index(request, context):

        # concert
        context['events'] = Event.objects.filter(
            is_published=True,
        )
        context['events_count'] = context['events'].count()

        try:
            socials = Social.objects.exclude(widget_code='').exclude(is_published=False)
            for widget in socials:
                context[widget.name + '_widget'] = widget
        except Social.DoesNotExist:
            pass

        return render(request, 'concerts.html', context)
