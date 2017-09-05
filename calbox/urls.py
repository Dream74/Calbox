from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'index'),
    url(r'^$',include('calbox.exam.urls') ),
)


urlpatterns += patterns('',
    url(r'^accounts/', include('calbox.accounts.urls')),
    url(r'^cal-x/', include('calbox.cal_x.urls')),
    #url(r'^testcode/', include('calbox.testcode.urls')),
    url(r'^exam/', include('calbox.exam.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^noscript/$', 'django.views.defaults.permission_denied' ),
)

urlpatterns += staticfiles_urlpatterns()
