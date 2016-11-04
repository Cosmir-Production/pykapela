
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from sitetree.sitetreeapp import register_i18n_trees

from . import views

admin.autodiscover()

urlpatterns = [

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^backoffice/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

urlpatterns += i18n_patterns(
    url(r'concerts/', include('meteleska.events.urls')),
    url(r'^$', views.WebView.as_view(), name='index'),
)

register_i18n_trees(['menu'])
