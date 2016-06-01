from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'me.views.name', name='name'),
    url(r'^home/', 'me.views.home', name='home'),
    url(r'^aboutme/', 'me.views.aboutme', name='aboutme'),
]
