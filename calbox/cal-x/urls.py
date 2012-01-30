from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('calbox.cal-x.views',
	(r'^$', 'code'),
	(r'^update_code/$', 'update_post_code'),
	#(r'^cal/$', 'cal.views.cal'),
)
