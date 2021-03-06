
from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings
from django.contrib import admin

from django.views.generic.simple import direct_to_template

admin.autodiscover()


from core.views import home

handler500 # Pyflakes

urlpatterns = patterns(
    '',
    url(r'^$',          home, name='home'),    
    url(r'^leaflets',   include('leaflets.urls')),        
    url(r'^parties',    include('parties.urls')),            
    url(r'^constituencies',    include('constituencies.urls')),                
    url(r'^analysis',   include('analysis.urls')),                    
    url(r'^tags',       include('tags.urls')),                        
    url(r'^categories', include('categories.urls')),                            
    url(r'^map/', include('boundaries.urls')),
    
    # Individual urls 
    url(r'^constituency/notspots/', direct_to_template, {'template': 'constituencies/notspots.html'}, name='constituency_notspots'),              
    url(r'^about/$', direct_to_template, {'template': 'core/about.html'}, name='about'),                
    url(r'^report/(?P<id>\d+)/sent/$', direct_to_template, {'template': 'core/report_sent.html'}, name='report_abuse_sent'),                            
    url(r'^report/(?P<id>\d+)/$', 'core.views.report_abuse', name='report_abuse'),                      
    
    # Administration URLS
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
