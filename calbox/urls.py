from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('calbox.views',
    url(r'^$', 'index'),
)
urlpatterns += patterns('',
		url(r'^accounts/', include('calbox.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
