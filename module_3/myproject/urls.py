from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openstack.views.Home', name='Home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    url(r'^opage1/', 'openstack.views.opage1',name='opage1'),
    url(r'^opage2/', 'openstack.views.opage2',name='opage2'),
    url(r'^opage3/', 'openstack.views.opage3',name='opage3'),
    url(r'^qrcode/', 'openstack.views.qrcode',name='qrcode'),
    url(r'^overv/', 'openstack.views.overv',name='overv'),
    url(r'^default/', 'openstack.views.default',name='default'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
