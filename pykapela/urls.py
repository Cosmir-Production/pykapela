
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.urls import re_path

from sitetree.sitetreeapp import register_i18n_trees

from . import views
from .gallery.views import GalleryView

admin.autodiscover()

urlpatterns = [

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^media/photologue/gallery/$', GalleryView.as_view(), name='gallery'),

    re_path(r'^media/photologue/', include('photologue.urls', namespace='photologue')),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

urlpatterns += i18n_patterns(
    url(r'concerts/', include('pykapela.events.urls')),
    url(r'^$', views.WebView.as_view(), name='index'),
)

register_i18n_trees(['main_menu'])
