from django.conf.urls.defaults import *

urlpatterns = patterns('django.contrib.auth.views',
                       (r'^login/$', 
                        'login', 
                        {'template_name': 'accounts/login.html'}),

                       (r'^logout/$', 
                        'logout', 
                        {'template_name': 'accounts/logged_out.html',
                        'next_page': '/cal-x/'}),

                       (r'^password_change/$', 
                        'password_change', 
                        {'template_name': 'accounts/password_change_form.html'}),

                       (r'^password_change/done/$', 
                        'password_change_done', 
                        {'template_name': 'accounts/password_change_done.html'}),

                       (r'^password_reset/$', 
                        'password_reset', 
                        {'template_name': 'accounts/password_reset_form.html',
                         'email_template_name': 'accounts/password_reset_email.html'}),

                       (r'^password_reset/done/$', 
                        'password_reset_done', 
                        {'template_name': 'accounts/password_reset_done.html'}),

                       (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
                        'password_reset_confirm', 
                        {'template_name': 'accounts/password_reset_confirm.html'}),

                       (r'^reset/done/$', 
                        'password_reset_complete', 
                        {'template_name': 'accounts/password_reset_complete.html'}),
)

urlpatterns += patterns('calbox.accounts.views',
                       (r'^signup/$', 
                        'signup', 
                        {'template_name': 'accounts/signup_form.html',
                         'email_template_name': 'accounts/signup_email.html'}),

                       (r'^signup/done/$', 
                        'signup_done', 
                        {'template_name': 'accounts/signup_done.html'}),

                       (r'^signup/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
                        'signup_confirm'),

                       (r'^signup/complete/$', 
                        'signup_complete', 
                        {'template_name': 'accounts/signup_complete.html'}),
)
