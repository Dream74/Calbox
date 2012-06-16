from django.conf.urls.defaults import patterns, include, url
from calbox.cal_x.question.models import Question_Code
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('calbox.cal_x.views',
	(r'^$', 'code', {'homework' : False}),
	(r'^homework$', 'code', {'homework' : True }),
	(r'^core/$', 'update_post_code', { 'com_run' : True} ),
	(r'^update_code/$', 'update_post_code', { 'com_run' : False}),
	(r'^doc/(\d+)$', 'question_doc'),
	(r'^example_code/(\d+)$', 'example_code'),
	(r'^mycode/$', 'mycode'),
	#(r'^cal/$', 'cal.views.cal'),
)
