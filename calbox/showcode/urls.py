from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('calbox.showcode.views',
	(r'^$', 'index'),
	#(r'^cal/$', 'cal.views.cal'),
)
