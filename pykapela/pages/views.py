from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.utils.translation import ugettext as _

from pykapela.base.views import BaseView
from pykapela.pages.models import Page


class PageView(BaseView):

    """
    Pages from DB
    """
    # @cache_page(settings.CACHE_VIEWS_DEFAULT_TIME)
    def get(self, request, slug='', *args, **kwargs):

        self.context = super()._prepare_context()

        if slug == '':
            raise Http404(_("Page not found. That's an error. Sorry. 404."))

        try:
            self.context['page'] = Page.objects.get(slug=slug, is_published=True)
        except Page.DoesNotExist:
            raise Http404(_("Page not found. That's an error. Sorry. 404."))

        return render(request, 'page.html', self.context)


def not_found_view(request, exception, *args, **kwargs):

    from pykapela.base.views import BaseView

    context = BaseView._prepare_context()

    return render(request, '404.html', context, status=404)
