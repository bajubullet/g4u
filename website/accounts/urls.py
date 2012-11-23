from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'logout/$', 'django.contrib.auth.views.logout_then_login',
        name='logout'),
    url(r'login/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'}, name='login'),
)

