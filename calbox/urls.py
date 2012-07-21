from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('calbox.views',
    #url(r'^$', 'index'),
    url(r'^$',include('calbox.cal_x.urls') ),

)

urlpatterns += patterns('',
		url(r'^accounts/', include('calbox.accounts.urls')),
		url(r'^cal-x/', include('calbox.cal_x.urls')),
		url(r'^testcode/', include('calbox.testcode.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^noscript/$', 'django.views.defaults.permission_denied' ),
)

urlpatterns += patterns('',
    url(r'^aboutus$', direct_to_template, {'template': 'aboutus.html'} ),
    url(r'^link$', direct_to_template, {'template': 'linkfriend.html'} ),
)
