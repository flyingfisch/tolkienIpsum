from django.conf.urls import url

from . import views

urlpatterns = [
    # Ex: /
    url(r'^$', views.index, name='index'),
    url(r'^generate$', views.generate, name='generate'),
]

