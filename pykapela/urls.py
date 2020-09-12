
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings
from django.urls import re_path, path

from sitetree.sitetreeapp import register_i18n_trees

from . import views
from .gallery.views import GalleryView, GalleryDetailView, PhotoView
from .pages.views import PageView

admin.autodiscover()

urlpatterns = [

    re_path(r'^favicon\.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),

    path('tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^media/photologue/gallery/(?P<slug>[\-\d\w]+)/$',
        GalleryDetailView.as_view(), name='gallery_detail'),
    url(r'^media/photologue/gallery/$', GalleryView.as_view(), name='gallery'),
    url(r'^media/photologue/photo/(?P<slug>[\-\d\w]+)/$', PhotoView.as_view(), name='photo'),

    re_path(r'^media/photologue/', include('photologue.urls', namespace='photologue')),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

    from django.contrib.staticfiles.views import serve
    urlpatterns.append(
        url(r'^static/(?P<path>.*)$', serve)
    )

urlpatterns += i18n_patterns(
    url(r'concerts', include('pykapela.events.urls')),
    url(r'concerts/', include('pykapela.events.urls')),


    url(r'^$', views.WebView.as_view(), name='index'),
    url(r'^(?P<slug>.*)$', PageView.as_view(), name='pages'),

)

register_i18n_trees(['main_menu'])
