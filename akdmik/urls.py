from django.conf.urls import patterns, include, url
from app.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', logoout, name='logout'),
)
