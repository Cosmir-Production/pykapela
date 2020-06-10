from django.shortcuts import render
from django.utils import timezone

from project.base.views import BaseView
from project.events.models import Event
from project.social.models import Social


class EventView(BaseView):

    """
    Concerts
    """
    # @cache_page(settings.CACHE_VIEWS_DEFAULT_TIME)
    def get(self, request, *args, **kwargs):

        self.context = super()._prepare_context()

        # concerts
        self.context['upcoming_events'] = Event.objects.filter(
            is_published=True,
            datetime__gte=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0),
        )
        self.context['events'] = Event.objects.filter(
            is_published=True,
            datetime__lte=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0),
        )

        return render(request, 'events/index.html', self.context)


class EventDetailView(BaseView):

    """
    Concerts
    """
    # @cache_page(settings.CACHE_VIEWS_DEFAULT_TIME)
    def get(self, request, slug, *args, **kwargs):

        self.context = super()._prepare_context()

        # concerts
        self.context['event'] = Event.objects.get(
            is_published=True,
            slug=slug,
        )

        return render(request, 'events/detail.html', self.context)
