from django.conf import settings
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.views import generic
from django.utils.translation import get_language

from pykapela.pages.models import Page
from pykapela.preferences.models import Preference
from pykapela.social.models import Social


class BaseView(generic.View):

    class Meta:
        abstract = True

    def __init__(self, **kwargs):
        super(BaseView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):

        context = self._prepare_context()

        view = getattr(self, request.resolver_match.view_name, None)
        return view(request, context, *args, **kwargs)

    @staticmethod
    def index(request, context):
        return HttpResponse("Sorry, nothing to be here...")

    @staticmethod
    def _prepare_context():
        context = {
            'SITE_NAME': settings.SITE_NAME,
            'SITE_URL': settings.SITE_URL,
            'SITE_URL_FULL': settings.SITE_URL_FULL,
            'CONTACT_PHONE': settings.CONTACT_PHONE,
            'CONTACT_EMAIL': settings.CONTACT_EMAIL,
        }

        preferences = Preference().get_values()
        context.update(preferences)

        # languages:
        context['languages'] = []
        context['current_language'] = get_language()
        for lang in settings.LANGUAGES:
            language = {
                'code': lang[0],
                'name': lang[1],
                'current': False,
                'flag': 'assets/img/flag-' + lang[0] + '.png'
            }
            if context['current_language'] == lang[0]:
                language['current'] = True

            context['languages'].append(language)

        socials = Social.objects.filter(
            is_published=True,
        ).order_by(
            'position',
        )
        context.update({
            "socials": socials
        })

        # widgets
        try:
            socials = Social.objects.exclude(widget_code='').exclude(is_published=False).order_by('position')
            for widget in socials:
                context.update({
                    widget.name + '_widget': widget,
                })
        except Social.DoesNotExist:
            pass

        try:
            pages = Page.objects.filter(is_published=True).order_by('position')

            for page in pages:
                context.update({
                    'page_' + page.slug: page
                })
        except IndexError as e:
            pass

        return context
