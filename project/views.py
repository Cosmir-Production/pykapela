from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import cache_page
from photologue.models import Photo, Gallery

from project.base.views import BaseView
from project.events.models import Event
from project.social.models import Social


class WebView(BaseView):

    """
    Homepage
    """
    @staticmethod
    # @cache_page(settings.CACHE_VIEWS_DEFAULT_TIME)
    def index(request, context):

        context['homepage'] = True

        # concert stay on homepage till this midnight
        context['events'] = Event.objects.filter(
            is_published=True,
            datetime__gte=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        )
        context['events_count'] = context['events'].count()

        try:
             socials = Social.objects.exclude(widget_code='').exclude(is_published=False)
             for widget in socials:
                context[widget.name + '_widget'] = widget
        except Social.DoesNotExist:
            pass

        try:
            context['images'] = Photo.objects.filter(sites__gallery=Gallery.objects.on_site().is_public().get(pk=1))[0:4]
        except Gallery.DoesNotExist:
            pass

        return render(request, 'index.html', context)
