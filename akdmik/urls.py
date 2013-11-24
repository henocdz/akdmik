from django.conf.urls import patterns, include, url
from app.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^alumnos/$', alumnos, name='alumnos'),
    url(r'^alumnos/nuevo/$', AlumnoNuevoView.as_view(), name='alumnos-nuevo'),
    url(r'^alumnos/editar/(?P<id>[0-9]{1,12})/$', AlumnoEditarView.as_view(), name='alumnos-editar'),
    url(r'^alumnos/eliminar/(?P<id>[0-9]{1,12})/$', alumnosEliminar, name='alumnos-eliminar'),
    url(r'^logout/$', logoout, name='logout'),
)
