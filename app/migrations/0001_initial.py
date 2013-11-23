# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AUser'
        db.create_table(u'app_auser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12, db_index=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ap_paterno', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ap_materno', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(default='1990-01-01')),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('estado', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('tipo', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['AUser'])

        # Adding M2M table for field groups on 'AUser'
        m2m_table_name = db.shorten_name(u'app_auser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('auser', models.ForeignKey(orm[u'app.auser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['auser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'AUser'
        m2m_table_name = db.shorten_name(u'app_auser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('auser', models.ForeignKey(orm[u'app.auser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['auser_id', 'permission_id'])

        # Adding model 'Materia'
        db.create_table(u'app_materia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyname', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['Materia'])

        # Adding model 'Grupo'
        db.create_table(u'app_grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('salon', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('capacidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Grupo'])

        # Adding model 'Clase'
        db.create_table(u'app_clase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Materia'])),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Grupo'])),
            ('profesor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.AUser'])),
        ))
        db.send_create_signal(u'app', ['Clase'])

        # Adding model 'Publicacion'
        db.create_table(u'app_publicacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.AUser'])),
            ('pertenece', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Clase'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'app', ['Publicacion'])

        # Adding model 'Horario'
        db.create_table(u'app_horario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dia', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('hora_inicio', self.gf('django.db.models.fields.TimeField')()),
            ('hora_fin', self.gf('django.db.models.fields.TimeField')()),
            ('clase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Clase'])),
        ))
        db.send_create_signal(u'app', ['Horario'])

        # Adding model 'Periodo'
        db.create_table(u'app_periodo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Clase'])),
            ('numero', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('inicio', self.gf('django.db.models.fields.DateField')()),
            ('fin', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'app', ['Periodo'])

        # Adding model 'Criterio'
        db.create_table(u'app_criterio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('puntaje', self.gf('django.db.models.fields.FloatField')()),
            ('periodo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Periodo'])),
        ))
        db.send_create_signal(u'app', ['Criterio'])

        # Adding model 'Asistencia'
        db.create_table(u'app_asistencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.AUser'])),
            ('clase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Clase'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'app', ['Asistencia'])

        # Adding model 'CalificacionCriterio'
        db.create_table(u'app_calificacioncriterio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.AUser'])),
            ('criterio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Criterio'])),
            ('puntaje', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app', ['CalificacionCriterio'])

        # Adding model 'Tak'
        db.create_table(u'app_tak', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Clase'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.AUser'])),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'app', ['Tak'])


    def backwards(self, orm):
        # Deleting model 'AUser'
        db.delete_table(u'app_auser')

        # Removing M2M table for field groups on 'AUser'
        db.delete_table(db.shorten_name(u'app_auser_groups'))

        # Removing M2M table for field user_permissions on 'AUser'
        db.delete_table(db.shorten_name(u'app_auser_user_permissions'))

        # Deleting model 'Materia'
        db.delete_table(u'app_materia')

        # Deleting model 'Grupo'
        db.delete_table(u'app_grupo')

        # Deleting model 'Clase'
        db.delete_table(u'app_clase')

        # Deleting model 'Publicacion'
        db.delete_table(u'app_publicacion')

        # Deleting model 'Horario'
        db.delete_table(u'app_horario')

        # Deleting model 'Periodo'
        db.delete_table(u'app_periodo')

        # Deleting model 'Criterio'
        db.delete_table(u'app_criterio')

        # Deleting model 'Asistencia'
        db.delete_table(u'app_asistencia')

        # Deleting model 'CalificacionCriterio'
        db.delete_table(u'app_calificacioncriterio')

        # Deleting model 'Tak'
        db.delete_table(u'app_tak')


    models = {
        u'app.asistencia': {
            'Meta': {'object_name': 'Asistencia'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.AUser']"}),
            'clase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Clase']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.auser': {
            'Meta': {'object_name': 'AUser'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ap_materno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'ap_paterno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'estado': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'default': "'1990-01-01'"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'tipo': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12', 'db_index': 'True'})
        },
        u'app.calificacioncriterio': {
            'Meta': {'object_name': 'CalificacionCriterio'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.AUser']"}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Criterio']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntaje': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.clase': {
            'Meta': {'object_name': 'Clase'},
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Grupo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Materia']"}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.AUser']"})
        },
        u'app.criterio': {
            'Meta': {'object_name': 'Criterio'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'periodo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Periodo']"}),
            'puntaje': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'salon': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'app.horario': {
            'Meta': {'object_name': 'Horario'},
            'clase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Clase']"}),
            'dia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hora_fin': ('django.db.models.fields.TimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.materia': {
            'Meta': {'object_name': 'Materia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyname': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'app.periodo': {
            'Meta': {'object_name': 'Periodo'},
            'clase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Clase']"}),
            'fin': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateField', [], {}),
            'numero': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'app.publicacion': {
            'Meta': {'object_name': 'Publicacion'},
            'creador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.AUser']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pertenece': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Clase']"})
        },
        u'app.tak': {
            'Meta': {'object_name': 'Tak'},
            'clase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Clase']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.AUser']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']