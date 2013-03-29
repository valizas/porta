# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'PersonaExterna.genero'
        db.delete_column('portapp_personaexterna', 'genero')

        # Deleting field 'Docente.genero'
        db.delete_column('portapp_docente', 'genero')

        # Deleting field 'Estudiante.genero'
        db.delete_column('portapp_estudiante', 'genero')


    def backwards(self, orm):
        
        # Adding field 'PersonaExterna.genero'
        db.add_column('portapp_personaexterna', 'genero', self.gf('django.db.models.fields.CharField')(default=None, max_length=15), keep_default=False)

        # Adding field 'Docente.genero'
        db.add_column('portapp_docente', 'genero', self.gf('django.db.models.fields.CharField')(default=None, max_length=15), keep_default=False)

        # Adding field 'Estudiante.genero'
        db.add_column('portapp_estudiante', 'genero', self.gf('django.db.models.fields.CharField')(default=None, max_length=15), keep_default=False)


    models = {
        'portapp.autorizaciondepublicacion': {
            'Meta': {'object_name': 'AutorizacionDePublicacion'},
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Docente']"}),
            'documento_a_publicar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Documento']"}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Estudiante']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'portapp.basecurso': {
            'Meta': {'object_name': 'BaseCurso'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'obs': ('django.db.models.fields.TextField', [], {}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Plan']"})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        'portapp.curso': {
            'Meta': {'object_name': 'Curso'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.BaseCurso']"}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'generacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Generacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {})
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
        'portapp.docentecurso': {
            'Meta': {'object_name': 'DocenteCurso'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Curso']"}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Docente']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'portapp.documento': {
            'Meta': {'object_name': 'Documento'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {}),
            'fecha_publicacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_subida': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
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
            'generacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Generacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'portapp.estudiantecurso': {
            'Meta': {'object_name': 'EstudianteCurso'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Curso']"}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Estudiante']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'portapp.feedbacksdelectura': {
            'Meta': {'object_name': 'FeedbacksDeLectura'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.QuienSolicitaDocumento']"}),
            'texto_feedback': ('django.db.models.fields.TextField', [], {})
        },
        'portapp.generacion': {
            'Meta': {'object_name': 'Generacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
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
        'portapp.plan': {
            'Meta': {'object_name': 'Plan'},
            'generacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Generacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True'})
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
