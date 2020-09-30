from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from photologue.models import Gallery, Photo
from photologue.views import GalleryListView

from pykapela.base.views import BaseView
from pykapela.photologue_custom.models import PykapelaGallery


class GalleryView(BaseView):

    """
    Galleries
    """
    @staticmethod
    def gallery(request, context, *args, **kwargs):

        context['object_list'] = PykapelaGallery.objects.on_site().is_public()

        return render(request, 'photologue/gallery_list.html', context)


class GalleryDetailView(BaseView):

    ordering = ['-date_added']

    """
    Gallery detail (all photos)
    """
    @staticmethod
    def gallery_detail(request, context, slug, *args, **kwargs):

        context['photos'] = Photo.objects.filter(galleries__slug=slug)
        try:
            context['gallery'] = context['photos'][0].galleries.last()
        except Exception as e:
            pass

        return render(request, 'photologue/gallery_detail.html', context)


class PhotoView(BaseView):

    ordering = ['-date_added']

    """
    Gallery detail (all photos)
    """
    @staticmethod
    def photo(request, context, slug, *args, **kwargs):

        photo = Photo.objects.get(slug=slug)

        context['object'] = photo
        context['gallery'] = photo.public_galleries()

        return render(request, 'photologue/photo_detail.html', context)
