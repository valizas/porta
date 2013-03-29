# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Generacion'
        db.create_table('portapp_generacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('portapp', ['Generacion'])

        # Adding model 'Plan'
        db.create_table('portapp_plan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('generacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Generacion'])),
            ('obs', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('portapp', ['Plan'])

        # Adding model 'Estudiante'
        db.create_table('portapp_estudiante', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('fecha_alta', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('generacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Generacion'])),
        ))
        db.send_create_signal('portapp', ['Estudiante'])

        # Adding model 'Coautoria'
        db.create_table('portapp_coautoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_alta', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('portapp', ['Coautoria'])

        # Adding model 'CoautoriaEstudiante'
        db.create_table('portapp_coautoriaestudiante', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Estudiante'])),
            ('coautoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Coautoria'])),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('stage', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fecha_verificado', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('portapp', ['CoautoriaEstudiante'])

        # Adding model 'Docente'
        db.create_table('portapp_docente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('fecha_alta', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('curriculum_academico', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('portapp', ['Docente'])

        # Adding model 'PersonaExterna'
        db.create_table('portapp_personaexterna', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('fecha_alta', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('adscripcion_institucional', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('curriculum_academico', self.gf('django.db.models.fields.TextField')()),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('portapp', ['PersonaExterna'])

        # Adding model 'BaseCurso'
        db.create_table('portapp_basecurso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('obs', self.gf('django.db.models.fields.TextField')()),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Plan'])),
            ('fecha_alta', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('portapp', ['BaseCurso'])

        # Adding model 'Curso'
        db.create_table('portapp_curso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.BaseCurso'])),
            ('generacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Generacion'])),
            ('obs', self.gf('django.db.models.fields.TextField')()),
            ('fecha_alta', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('portapp', ['Curso'])

        # Adding model 'DocenteCurso'
        db.create_table('portapp_docentecurso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Docente'])),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Curso'])),
        ))
        db.send_create_signal('portapp', ['DocenteCurso'])

        # Adding model 'EstudianteCurso'
        db.create_table('portapp_estudiantecurso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Estudiante'])),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Curso'])),
        ))
        db.send_create_signal('portapp', ['EstudianteCurso'])

        # Adding model 'Documento'
        db.create_table('portapp_documento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')()),
            ('fecha_subida', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fecha_publicacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('texto_completo', self.gf('django.db.models.fields.TextField')()),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('portapp', ['Documento'])

        # Adding model 'DocumentoEstudiante'
        db.create_table('portapp_documentoestudiante', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('documento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Documento'])),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Estudiante'])),
        ))
        db.send_create_signal('portapp', ['DocumentoEstudiante'])

        # Adding model 'DocumentoCoautoria'
        db.create_table('portapp_documentocoautoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('documento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Documento'])),
            ('coautoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Coautoria'])),
        ))
        db.send_create_signal('portapp', ['DocumentoCoautoria'])

        # Adding model 'AutorizacionDePublicacion'
        db.create_table('portapp_autorizaciondepublicacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('documento_a_publicar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Documento'])),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Estudiante'])),
            ('docente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Docente'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('portapp', ['AutorizacionDePublicacion'])

        # Adding model 'DenegacionDeSolicitudes'
        db.create_table('portapp_denegaciondesolicitudes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('solicitud_denegada', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.SolicitudDeDocumentoPublicado'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('portapp', ['DenegacionDeSolicitudes'])

        # Adding model 'QuienSolicitaDocumento'
        db.create_table('portapp_quiensolicitadocumento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_libre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Estudiante'])),
            ('docente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Docente'])),
            ('persona_registrada', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.PersonaExterna'])),
        ))
        db.send_create_signal('portapp', ['QuienSolicitaDocumento'])

        # Adding model 'SolicitudDeDocumentoPublicado'
        db.create_table('portapp_solicituddedocumentopublicado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quien', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.QuienSolicitaDocumento'])),
            ('documento_solicitado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.Documento'])),
            ('texto_fundamento', self.gf('django.db.models.fields.TextField')()),
            ('fecha_solicitud', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('portapp', ['SolicitudDeDocumentoPublicado'])

        # Adding model 'FeedbacksDeLectura'
        db.create_table('portapp_feedbacksdelectura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quien', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.QuienSolicitaDocumento'])),
            ('texto_feedback', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('portapp', ['FeedbacksDeLectura'])

        # Adding model 'BusquedasLibres'
        db.create_table('portapp_busquedaslibres', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quien', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portapp.QuienSolicitaDocumento'])),
            ('texto_buscado', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('portapp', ['BusquedasLibres'])

        # Adding model 'ResultadosDeBusqueda'
        db.create_table('portapp_resultadosdebusqueda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('busqueda', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('portapp', ['ResultadosDeBusqueda'])

        # Adding M2M table for field documentos on 'ResultadosDeBusqueda'
        db.create_table('portapp_resultadosdebusqueda_documentos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resultadosdebusqueda', models.ForeignKey(orm['portapp.resultadosdebusqueda'], null=False)),
            ('documento', models.ForeignKey(orm['portapp.documento'], null=False))
        ))
        db.create_unique('portapp_resultadosdebusqueda_documentos', ['resultadosdebusqueda_id', 'documento_id'])


    def backwards(self, orm):
        
        # Deleting model 'Generacion'
        db.delete_table('portapp_generacion')

        # Deleting model 'Plan'
        db.delete_table('portapp_plan')

        # Deleting model 'Estudiante'
        db.delete_table('portapp_estudiante')

        # Deleting model 'Coautoria'
        db.delete_table('portapp_coautoria')

        # Deleting model 'CoautoriaEstudiante'
        db.delete_table('portapp_coautoriaestudiante')

        # Deleting model 'Docente'
        db.delete_table('portapp_docente')

        # Deleting model 'PersonaExterna'
        db.delete_table('portapp_personaexterna')

        # Deleting model 'BaseCurso'
        db.delete_table('portapp_basecurso')

        # Deleting model 'Curso'
        db.delete_table('portapp_curso')

        # Deleting model 'DocenteCurso'
        db.delete_table('portapp_docentecurso')

        # Deleting model 'EstudianteCurso'
        db.delete_table('portapp_estudiantecurso')

        # Deleting model 'Documento'
        db.delete_table('portapp_documento')

        # Deleting model 'DocumentoEstudiante'
        db.delete_table('portapp_documentoestudiante')

        # Deleting model 'DocumentoCoautoria'
        db.delete_table('portapp_documentocoautoria')

        # Deleting model 'AutorizacionDePublicacion'
        db.delete_table('portapp_autorizaciondepublicacion')

        # Deleting model 'DenegacionDeSolicitudes'
        db.delete_table('portapp_denegaciondesolicitudes')

        # Deleting model 'QuienSolicitaDocumento'
        db.delete_table('portapp_quiensolicitadocumento')

        # Deleting model 'SolicitudDeDocumentoPublicado'
        db.delete_table('portapp_solicituddedocumentopublicado')

        # Deleting model 'FeedbacksDeLectura'
        db.delete_table('portapp_feedbacksdelectura')

        # Deleting model 'BusquedasLibres'
        db.delete_table('portapp_busquedaslibres')

        # Deleting model 'ResultadosDeBusqueda'
        db.delete_table('portapp_resultadosdebusqueda')

        # Removing M2M table for field documentos on 'ResultadosDeBusqueda'
        db.delete_table('portapp_resultadosdebusqueda_documentos')


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
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
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
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
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
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'portapp.plan': {
            'Meta': {'object_name': 'Plan'},
            'generacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portapp.Generacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'obs': ('django.db.models.fields.TextField', [], {})
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
