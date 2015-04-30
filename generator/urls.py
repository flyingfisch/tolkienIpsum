from django.conf.urls import url

from . import views

urlpatterns = [
    # Ex: /generator/
    url(r'^$', views.index, name='index'),

    # Ex: /generator/1/2/3
    url(r'^(?P<paragraphs>[0-9]+)/(?P<sentenceMin>[0-9]+)/(?P<sentenceMax>[0-9]+)/$', views.index, name='index'),
]
