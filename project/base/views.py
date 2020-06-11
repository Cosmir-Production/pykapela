from django.conf import settings
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.views import generic

from project.preferences.models import Preference
from project.social.models import Social


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

        socials = Social.objects.filter(
            is_published=True,
        )
        context.update({
            "socials": socials
        })
        return context
