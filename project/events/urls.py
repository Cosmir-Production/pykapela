
from django.conf.urls import url
from django.urls import re_path, path

from .views import EventView, EventDetailView

urlpatterns = [

    path('<slug>/', EventDetailView.as_view(), name='concert'),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    url(r'^$', EventView.as_view(), name='concerts'),
    # url(r'^$', views.index, name='index'),
]
