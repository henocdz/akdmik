from django.conf.urls import patterns, include, url
from app.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),

    # -------- ADMINISTRADOR
    url(r'^alumnos/$', alumnos, name='alumnos'),
    url(r'^alumnos/nuevo/$', AlumnoNuevoView.as_view(), name='alumnos-nuevo'),
    url(r'^alumnos/editar/(?P<id>[0-9]{1,12})/$', AlumnoEditarView.as_view(), name='alumnos-editar'),
    url(r'^alumnos/eliminar/(?P<id>[0-9]{1,12})/$', alumnosEliminar, name='alumnos-eliminar'),

    url(r'^profesores/$', profesores, name='profesores'),
    url(r'^profesores/nuevo/$', ProfesorNuevoView.as_view(), name='profesores-nuevo'),
    url(r'^profesores/editar/(?P<id>[0-9]{1,12})/$', ProfesorEditarView.as_view(), name='profesores-editar'),
    url(r'^profesores/eliminar/(?P<id>[0-9]{1,12})/$', profesorEliminar, name='profesores-eliminar'),

    url(r'^materias/$', materias, name='materias'),
    url(r'^materias/nuevo/$', MateriaNuevoView.as_view(), name='materias-nuevo'),
    url(r'^materias/editar/(?P<id>[0-9]{1,12})/$', MateriaEditarView.as_view(), name='materias-editar'),

    url(r'^grupos/$', grupos, name='grupos'),
    url(r'^grupos/nuevo/$', GrupoNuevoView.as_view(), name='grupos-nuevo'),
    url(r'^grupos/editar/(?P<id>[0-9]{1,12})/$', GrupoEditarView.as_view(), name='grupos-editar'),

    url(r'^clases/$', clases, name='clases'),
    url(r'^clases/nuevo/$', ClaseNuevoView.as_view(), name='clases-nuevo'),
    url(r'^clases/editar/(?P<id>[0-9]{1,12})/$', ClaseEditarView.as_view(), name='clases-editar'),  

    url(r'^horarios/$', horarios, name='horarios'),
    url(r'^horarios/nuevo/$', HorarioNuevoView.as_view(), name='horarios-nuevo'),
    url(r'^horarios/editar/(?P<id>[0-9]{1,12})/$', HorarioEditarView.as_view(), name='horarios-editar'),  
    
    # -------- ALUMNOS

    # -------- PROFESORES

    # url(r'^grupos/$', grupos, name='grupos'),
    # url(r'^grupos/nuevo/$', GrupoNuevoView.as_view(), name='grupos-nuevo'),
    # url(r'^grupos/editar/(?P<id>[0-9]{1,12})/$', GrupoEditarView.as_view(), name='grupos-editar'),

    # -------- REALTIME PATHs



    # -------- GENERAL
    url(r'^$', 'app.views.home', name='home'),

    #---------- USUARIO
    url(r'^u/(?P<username>[a-zA-Z0-9]{1,12})/$', 'app.views.perfil', name="perfil"),

    #-------- GRUPOS
    url(r'^grupo/(?P<nombre>[a-zA-Z0-9._]{2,})/$', 'app.views.grupo', name="grupo"),

    #----- INSCRIPCION
    url(r'^inscripcion/$', 'app.views.inscripcion', name="inscripcion"),
    url(r'^inscripcion/inscribir/$', inscribir, name="inscribir-clase"),

    url(r'^logout/$', logoout, name='logout'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    
    url(r'^admin/', include(admin.site.urls)),
)
