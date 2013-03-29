# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Docente.user'
        db.delete_column('portapp_docente', 'user_id')

        # Deleting field 'PersonaExterna.user'
        db.delete_column('portapp_personaexterna', 'user_id')

        # Deleting field 'Estudiante.user'
        db.delete_column('portapp_estudiante', 'user_id')


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Docente.user'
        raise RuntimeError("Cannot reverse this migration. 'Docente.user' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PersonaExterna.user'
        raise RuntimeError("Cannot reverse this migration. 'PersonaExterna.user' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Estudiante.user'
        raise RuntimeError("Cannot reverse this migration. 'Estudiante.user' and its values cannot be restored.")


    models = {
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
