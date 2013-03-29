# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'PersonaExterna.user'
        db.add_column('portapp_personaexterna', 'user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True), keep_default=False)

        # Adding field 'Docente.user'
        db.add_column('portapp_docente', 'user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True), keep_default=False)

        # Adding field 'Estudiante.user'
        db.add_column('portapp_estudiante', 'user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'PersonaExterna.user'
        db.delete_column('portapp_personaexterna', 'user_id')

        # Deleting field 'Docente.user'
        db.delete_column('portapp_docente', 'user_id')

        # Deleting field 'Estudiante.user'
        db.delete_column('portapp_estudiante', 'user_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'portapp.autorizaciondepublicacion': {
            'Meta': {'object_name': 'AutorizacionDePublicacion'},
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Docente']"}),
            'documento_a_publicar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Documento']"}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Estudiante']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'portapp.busquedaslibres': {
            'Meta': {'object_name': 'BusquedasLibres'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.QuienSolicitaDocumento']"}),
            'texto_buscado': ('django.db.models.fields.TextField', [], {})
        },
        'portapp.coautoria': {
            'Meta': {'object_name': 'Coautoria'},
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seudonimo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'portapp.coautoriaestudiante': {
            'Meta': {'object_name': 'CoautoriaEstudiante'},
            'coautoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Coautoria']"}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Estudiante']"}),
            'fecha_ingreso': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_verificado': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stage': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'portapp.denegaciondesolicitudes': {
            'Meta': {'object_name': 'DenegacionDeSolicitudes'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'solicitud_denegada': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.SolicitudDeDocumentoPublicado']"})
        },
        'portapp.docente': {
            'Meta': {'object_name': 'Docente'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'curriculum_academico': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True'})
        },
        'portapp.documento': {
            'Meta': {'object_name': 'Documento'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'docente_referente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Docente']", 'null': 'True'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {}),
            'fecha_publicacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_subida': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'texto_completo': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'portapp.documentocoautoria': {
            'Meta': {'object_name': 'DocumentoCoautoria'},
            'coautoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Coautoria']"}),
            'documento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Documento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'portapp.documentoestudiante': {
            'Meta': {'object_name': 'DocumentoEstudiante'},
            'documento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Documento']"}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Estudiante']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'portapp.estudiante': {
            'Meta': {'object_name': 'Estudiante'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True'})
        },
        'portapp.feedbacksdelectura': {
            'Meta': {'object_name': 'FeedbacksDeLectura'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.QuienSolicitaDocumento']"}),
            'texto_feedback': ('django.db.models.fields.TextField', [], {})
        },
        'portapp.personaexterna': {
            'Meta': {'object_name': 'PersonaExterna'},
            'adscripcion_institucional': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'curriculum_academico': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True'})
        },
        'portapp.quiensolicitadocumento': {
            'Meta': {'object_name': 'QuienSolicitaDocumento'},
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Docente']"}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Estudiante']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_libre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'persona_registrada': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.PersonaExterna']"})
        },
        'portapp.resultadosdebusqueda': {
            'Meta': {'object_name': 'ResultadosDeBusqueda'},
            'busqueda': ('django.db.models.fields.TextField', [], {}),
            'documentos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portapp.Documento']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'portapp.solicituddedocumentopublicado': {
            'Meta': {'object_name': 'SolicitudDeDocumentoPublicado'},
            'documento_solicitado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Documento']"}),
            'fecha_solicitud': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.QuienSolicitaDocumento']"}),
            'texto_fundamento': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['portapp']
