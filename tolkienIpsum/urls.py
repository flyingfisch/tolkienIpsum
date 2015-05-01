from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'tolkienIpsum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('home.urls')),
    url(r'^generator/', include('generator.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
