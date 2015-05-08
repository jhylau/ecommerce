from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    url(r'^members/', include('members.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
