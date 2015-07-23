from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home-index'),
    url(r'^section/(?P<section_name>[^/]+)/$', views.section, name='home-section'),
    url(r'^article/(?P<article_id>[^/]+)/$', views.article, name='home-article'),
]
