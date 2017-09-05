from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('calbox.testcode.views',
	(r'^$', 'index'),
	(r'^core/$', 'update_post_code'),
	#(r'^cal/$', 'cal.views.cal'),
)
