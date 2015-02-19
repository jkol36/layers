from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'layers.profiles.views.home', name='home'),
     url(r'^my_account/', 'layers.profiles.views.my_account', name='my_account'),
     url(r'get_started/', 'layers.get_started.views.get_started', name='get_started'),
     url(r'submit_design/', 'layers.get_started.views.submit_design', name='submit_design'),
     url(r'^complete_signup/$', 'layers.profiles.views.complete_signup', name='complete_signup'),
	 url(r'^my_account/$', 'layers.profiles.views.my_account', name='my_account'),    
     url(r'^logout/$', 'layers.profiles.views.logout_view', name='logout'),
     url(r'^login$', 'layers.landing.views.login_view', name='login'),
     url(r'^update_settings$', 'layers.profiles.views.update_settings', name='update_settings'),
     url(r'^add_project$', 'layers.projects.views.add_project', name='add_project'),
     url(r'^add_photo/(\d+)/$', 'layers.projects.views.add_photo_to_project', name='add_photo'),
     url(r'^signup$', 'layers.landing.views.signup_view', name='signup'),
     url(r'^faq$', 'layers.landing.views.faq', name='faq'),
     url(r'^blog$', 'layers.landing.views.blog', name='blog'),
     url(r'^about$', 'layers.landing.views.about', name='about'),
     url(r'^contact$', 'layers.landing.views.contact', name='contact'),
     url(r'^privacy$', 'layers.landing.views.privacy', name='privacy'),
     url(r'^terms$', 'layers.landing.views.terms', name='terms'),
     url(r'^project_status/(\d+)/$', 'layers.projects.views.project_status', name='project_status'),
     url(r'^signup_for_emails$', 'layers.subscribe.views.signup_for_emails', name='signup_for_emails'),
     url(r'^all_projects$', 'layers.projects.views.all_projects', name='all_projects'),
     url(r'^edit_project/(\d+)/$', 'layers.projects.views.edit_project', name='edit_project'),
     url(r'^start_project/(\d+)/$', 'layers.projects.views.start_project', name='start_project'),
     url(r'^bid_project/(\d+)/$', 'layers.projects.views.bid_project', name='bid_project'),

    # url(r'^blog/', include('blog.urls')),

     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
