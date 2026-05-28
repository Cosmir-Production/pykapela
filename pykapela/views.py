from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone, translation
from photologue.models import Photo, Gallery

from pykapela.base.views import BaseView
from pykapela.events.models import Event
from pykapela.pages.models import Page
from pykapela.photologue_custom.models import PykapelaGallery


AI_CRAWLERS = (
    'GPTBot',
    'PerplexityBot',
    'Google-Extended',
    'ClaudeBot',
    'CCBot',
)

# Explicit top-level routes win over the catch-all PageView.
RESERVED_PAGE_SLUGS = (
    'concerts',
    'gallery',
)


def _site_root():
    return settings.SITE_URL_FULL.rstrip('/')


def _absolute_url(path):
    return '%s%s' % (_site_root(), path)


def _format_lastmod(value):
    if value is None:
        return None
    return value.date().isoformat()


def _sitemap_entry(view_name, kwargs=None, lastmod=None):
    kwargs = kwargs or {}
    alternate_urls = []

    for language_code, _ in settings.LANGUAGES:
        with translation.override(language_code):
            alternate_urls.append({
                'hreflang': language_code,
                'href': _absolute_url(reverse(view_name, kwargs=kwargs)),
            })

    default_language = getattr(settings, 'PREFIX_DEFAULT_LANGUAGE', settings.LANGUAGES[0][0])
    default_url = next(
        (alternate['href'] for alternate in alternate_urls if alternate['hreflang'] == default_language),
        alternate_urls[0]['href'],
    )

    return {
        'loc': default_url,
        'alternates': alternate_urls,
        'x_default': default_url,
        'lastmod': _format_lastmod(lastmod),
    }


def _sitemap_entries():
    entries = [
        _sitemap_entry('index'),
        _sitemap_entry('concerts'),
        _sitemap_entry('gallery'),
    ]

    pages = Page.objects.filter(
        is_published=True,
    ).exclude(
        slug__isnull=True,
    ).exclude(
        slug='',
    ).exclude(
        slug__in=RESERVED_PAGE_SLUGS,
    ).order_by(
        'slug',
    )
    for page in pages:
        entries.append(_sitemap_entry('pages', kwargs={'slug': page.slug}, lastmod=page.changed))

    events = Event.objects.filter(
        is_published=True,
    ).order_by(
        'datetime',
        'slug',
    )
    for event in events:
        entries.append(_sitemap_entry('concert', kwargs={'slug': event.slug}, lastmod=event.changed))

    galleries = PykapelaGallery.objects.on_site().is_public().exclude(
        slug__isnull=True,
    ).exclude(
        slug='',
    ).order_by(
        'slug',
    )
    for gallery in galleries:
        entries.append(_sitemap_entry('gallery_detail', kwargs={'slug': gallery.slug}))

    return entries


def robots_txt(request):
    context = {
        'ai_crawlers': AI_CRAWLERS,
        'sitemap_url': '%s/sitemap.xml' % _site_root(),
    }
    return render(request, 'robots.txt', context, content_type='text/plain')


def sitemap_xml(request):
    context = {
        'url_entries': _sitemap_entries(),
    }
    return render(request, 'sitemap.xml', context, content_type='application/xml')


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
