from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('calbox.exam.views',
	(r'^core/$', 'update_post_code'),
	(r'^getInputList/$', 'get_input'),
	#(r'^cal/$', 'cal.views.cal'),
)

urlpatterns += patterns('calbox.cal_x.views',
  (r'^$', 'code', {'homework' : False, 'template_name' : 'exam/index.html' }),
)

