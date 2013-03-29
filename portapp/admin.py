#  coding: utf-8

from django.contrib import admin
from portapp.models import *    


#class GeneracionAdmin(admin.ModelAdmin):
#    pass
#class PlanAdmin(admin.ModelAdmin):
#    pass
class EstudianteAdmin(admin.ModelAdmin):
    pass
class CoautoriaAdmin(admin.ModelAdmin):
    pass
class CoautoriaEstudianteAdmin(admin.ModelAdmin):
    pass
class DocenteAdmin(admin.ModelAdmin):
    pass
class PersonaExternaAdmin(admin.ModelAdmin):
    pass
#class BaseCursoAdmin(admin.ModelAdmin):
#    pass
#class CursoAdmin(admin.ModelAdmin):
#    pass
#class DocenteCursoAdmin(admin.ModelAdmin):
#    pass
#class EstudianteCursoAdmin(admin.ModelAdmin):
#    pass
class DocumentoAdmin(admin.ModelAdmin):
    pass
class DocumentoEstudianteAdmin(admin.ModelAdmin):
    pass
class DocumentoCoautoriaAdmin(admin.ModelAdmin):
    pass
class AutorizacionDePublicacionAdmin(admin.ModelAdmin):
    pass
class DenegacionDeSolicitudesAdmin(admin.ModelAdmin):
    pass
class QuienSolicitaDocumentoAdmin(admin.ModelAdmin):
    pass
class SolicitudDeDocumentoPublicadoAdmin(admin.ModelAdmin):
    pass
class FeedbacksDeLecturaAdmin(admin.ModelAdmin):
    pass
class BusquedasLibresAdmin(admin.ModelAdmin):
    pass
class ResultadosDeBusquedaAdmin(admin.ModelAdmin):
    pass

#admin.site.register( Generacion,GeneracionAdmin)
#admin.site.register( Plan,PlanAdmin)
admin.site.register( Estudiante,EstudianteAdmin)
admin.site.register( Coautoria,CoautoriaAdmin)
admin.site.register( CoautoriaEstudiante,CoautoriaEstudianteAdmin)
admin.site.register( Docente,DocenteAdmin)
admin.site.register( PersonaExterna,PersonaExternaAdmin)
#admin.site.register( BaseCurso,BaseCursoAdmin)
#admin.site.register( Curso,CursoAdmin)
#admin.site.register( DocenteCurso,DocenteCursoAdmin)
#admin.site.register( EstudianteCurso,EstudianteCursoAdmin)
admin.site.register( Documento,DocumentoAdmin)
admin.site.register( DocumentoEstudiante,DocumentoEstudianteAdmin)
admin.site.register( DocumentoCoautoria,DocumentoCoautoriaAdmin)
admin.site.register( AutorizacionDePublicacion,AutorizacionDePublicacionAdmin)
admin.site.register( DenegacionDeSolicitudes,DenegacionDeSolicitudesAdmin)
admin.site.register( QuienSolicitaDocumento,QuienSolicitaDocumentoAdmin)
admin.site.register( SolicitudDeDocumentoPublicado,SolicitudDeDocumentoPublicadoAdmin)
admin.site.register( FeedbacksDeLectura,FeedbacksDeLecturaAdmin)
admin.site.register( BusquedasLibres,BusquedasLibresAdmin)
admin.site.register( ResultadosDeBusqueda,ResultadosDeBusquedaAdmin)

