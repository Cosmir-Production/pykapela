from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from photologue.models import Gallery, Photo
from photologue.views import GalleryListView

from pykapela.base.views import BaseView
from pykapela.photologue_custom.models import GalleryExtended


class GalleryView(BaseView):

    """
    Galleries
    """
    @staticmethod
    def gallery(request, context, *args, **kwargs):

        context['object_list'] = Gallery.objects.on_site().is_public()

        return render(request, 'photologue/gallery_list.html', context)
