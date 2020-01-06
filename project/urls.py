
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.urls import re_path

from sitetree.sitetreeapp import register_i18n_trees

from . import views

admin.autodiscover()

urlpatterns = [

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^images/', include('photologue.urls', namespace='photologue')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

urlpatterns += i18n_patterns(
    url(r'concerts/', include('project.events.urls')),
    url(r'^$', views.WebView.as_view(), name='index'),
)

register_i18n_trees(['main_menu'])
