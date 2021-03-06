from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import cache_page
from photologue.models import Photo, Gallery

from pykapela.base.views import BaseView
from pykapela.events.models import Event
from pykapela.social.models import Social


class WebView(BaseView):

    """
    Homepage
    """
    @staticmethod
    # @cache_page(settings.CACHE_VIEWS_DEFAULT_TIME)
    def index(request, context):

        context['homepage'] = True

        # concert stay on homepage three more hours
        context['upcoming_events'] = Event.objects.filter(
            is_published=True,
            datetime__gte=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timezone.timedelta(hours=3)
        ).order_by(
            '-is_promoted',
            'datetime'
        )
        context['upcoming_events_count'] = context['upcoming_events'].count()


        try:
            context['images'] = Photo.objects.filter(galleries=context['config_promoted_gallery'])[0:10]
        except Gallery.DoesNotExist:
            pass

        return render(request, 'index.html', context)
