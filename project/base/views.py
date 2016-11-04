from django.http import HttpResponse
from django.views import generic


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
        context = {'title': 'METELESKA'}
        return context
