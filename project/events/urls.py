
from django.conf.urls import url

from .views import EventView

urlpatterns = [

    url(r'^$', EventView.as_view(), name='concerts'),
    # url(r'^$', views.index, name='index'),
]
