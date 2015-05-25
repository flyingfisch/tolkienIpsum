from django.conf.urls import url

from . import views

urlpatterns = [
    # Ex: /
    url(r'^$', views.index, name='index')
]

