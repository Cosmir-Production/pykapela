from django.shortcuts import render
from django.utils import timezone

from pykapela.base.views import BaseView
from pykapela.events.models import Event
from pykapela.social.models import Social


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
            datetime__gte=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timezone.timedelta(hours=3),
        )
        self.context['upcoming_events_count'] = self.context['upcoming_events'].count()

        self.context['archive_events'] = Event.objects.filter(
            is_published=True,
            datetime__lte=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timezone.timedelta(hours=3),
        )
        self.context['archive_events_count'] = self.context['archive_events'].count()

        return render(request, 'events/index.html', self.context)


class EventDetailView(BaseView):

    """
    Concert detail
    """
    # @cache_page(settings.CACHE_VIEWS_DEFAULT_TIME)
    def get(self, request, slug=None, *args, **kwargs):

        self.context = super()._prepare_context()

        # concerts
        self.context['event'] = Event.objects.get(
            is_published=True,
            slug=slug,
        )

        return render(request, 'events/detail.html', self.context)
