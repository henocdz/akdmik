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


    url(r'^profesores/$', profesores, name='profesores'),
    url(r'^profesores/nuevo/$', ProfesorNuevoView.as_view(), name='profesores-nuevo'),
    url(r'^profesores/editar/(?P<id>[0-9]{1,12})/$', ProfesorEditarView.as_view(), name='profesores-editar'),
    url(r'^profesores/eliminar/(?P<id>[0-9]{1,12})/$', profesorEliminar, name='profesores-eliminar'),

    url(r'^logout/$', logoout, name='logout'),
)
