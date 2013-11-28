# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Boletin.fecha'
        db.delete_column(u'app_boletin', 'fecha')

        # Adding field 'Boletin.date'
        db.add_column(u'app_boletin', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 11, 25, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Boletin.fecha'
        db.add_column(u'app_boletin', 'fecha',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default='2013-11-25', blank=True),
                      keep_default=False)

        # Deleting field 'Boletin.date'
        db.delete_column(u'app_boletin', 'date')


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
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ap_materno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'ap_paterno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': 'None', 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'default': "'1993-01-01'"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12', 'db_index': 'True'})
        },
        u'app.boletin': {
            'Meta': {'object_name': 'Boletin'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.AUser']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'app.calificacioncriterio': {
            'Meta': {'object_name': 'CalificacionCriterio'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.AUser']"}),
            'criterio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Criterio']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntaje': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.clase': {
            'Meta': {'unique_together': "(('materia', 'grupo', 'profesor'),)", 'object_name': 'Clase'},
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
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'salon': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'})
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
            'keyname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
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
        u'app.task': {
            'Meta': {'object_name': 'Task'},
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