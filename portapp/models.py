# coding: utf-8

#       (C) 2011 by Jorge Chávez, Paribanú Freitas & Haroldo Stenger (UDELAR, Facultad de Psicología)
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from django.db import models
from django.db.models import CharField, ForeignKey
from django.db.models import TextField, EmailField, DateField
from django.db.models import DateTimeField, ManyToManyField
from django.contrib.auth.models import User
from porta.portapp.globales import AVATARS

#from string import trim
#class Generacion(models.Model):
#    year = IntegerField()
#
#    class Meta:
#        verbose_name_plural = u'Generaciones'
#
#    def __unicode__(self):
#        return str(self.year)
#
#class Plan(models.Model):
#    nombre = CharField(max_length=30)
#    generacion = ForeignKey(Generacion)
#    obs = TextField(blank=True)
#    
#
#    class Meta:
#        verbose_name_plural = u'Planes'
#
#    def __unicode__(self):
#        return self.nombre

class Persona(models.Model):
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    cedula = CharField(max_length=10)
    email = EmailField()
    fecha_alta = DateTimeField(auto_now=False, auto_now_add=True)
#    user=models.OneToOneField(User) south
    user=models.OneToOneField(User, null=True)
    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s %s" % (self.nombre.capitalize(), self.apellido.capitalize())

    def clean(self):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        return super(Persona, self).clean()
        
    def save(self):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        super(Persona, self).save()

class Estudiante(Persona):
    pass

class Coautoria(models.Model):
    seudonimo = models.CharField(max_length=50, unique=True)
    fecha_alta = DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        return self.seudonimo.capitalize()

    def clean(self):
        self.seudonimo = self.seudonimo.upper()
        return super(Coautoria, self).clean()
        
    def save(self):
        self.seudonimo = self.seudonimo.upper()
        super(Coautoria, self).save()

class CoautoriaEstudiante(models.Model):
    estudiante = ForeignKey(Estudiante)
    coautoria = ForeignKey(Coautoria)
    fecha_ingreso = DateTimeField(auto_now=True, auto_now_add=True)
    stage = CharField(max_length=20, choices=[ ('CREADOR','CREADOR'),
                                               ('PROPUESTO','PROPUESTO'),
                                               ('AUTO-PROPUESTO','AUTO-PROPUESTO'),
                                               ('VERIFICADO','VERIFICADO')
                                             ])
    fecha_verificado = DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = u'Estudiantes pertenecientes a una coautoría'
        unique_together=('estudiante', 'coautoria')

    def es_miembro_pleno(self):
        return self.stage=='CREADOR' or self.stage=='VERIFICADO'

    def __unicode__(self):
        return u"%s > %s" % (self.estudiante, self.coautoria)

class Docente(Persona):
    curriculum_academico = TextField()

class PersonaExterna(Persona):
    adscripcion_institucional = CharField(max_length=50)
    curriculum_academico = TextField()
    pais = CharField(max_length=30)

    class Meta:
        verbose_name_plural = u'Personas externas'

class Asignatura(models.Model):
    denominacion = CharField(max_length=100)
    

class Documento(models.Model):
    titulo = CharField(max_length=60)
    fecha_creacion = DateField(blank=False)
    fecha_subida = DateTimeField(auto_now=False, auto_now_add=True)
    fecha_publicacion = DateTimeField(auto_now=False, auto_now_add=True)
    docente_referente = ForeignKey('Docente', null=True)
    abstract = TextField()
    keywords = TextField()
    texto_completo = TextField(blank=True)
    path = CharField(max_length=1024)
    ## enganchar con Asignatura a la que está inscripto este Documento-trabajo.  (pari dixit, 27/3/2012)
    asignatura = ForeignKey(Asignatura,  null=True,  blank=True)
    def __unicode__(self):
        return "%s %s" % (self.titulo, self.path)

class DocumentoEstudiante(models.Model):
    documento = ForeignKey(Documento)
    estudiante = ForeignKey(Estudiante)

    class Meta:
        verbose_name_plural = u'Autorías de estudiante único de documentos'

class DocumentoCoautoria(models.Model):
    documento = ForeignKey(Documento)
    coautoria = ForeignKey(Coautoria)

    class Meta:
        verbose_name_plural = u'Co-autorías de documentos'

class AutorizacionDePublicacion(models.Model):
    documento_a_publicar = ForeignKey(Documento)
    estudiante = ForeignKey(Estudiante)
    docente = ForeignKey(Docente)
    fecha = DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = u'Autorización de publicaciones'

class DenegacionDeSolicitudes(models.Model):
    solicitud_denegada = ForeignKey('SolicitudDeDocumentoPublicado')
    fecha = DateTimeField(auto_now=False, auto_now_add=True)
    observaciones = TextField()

    class Meta:
        verbose_name_plural = u'Denegaciones de solicitudes'

class QuienSolicitaDocumento(models.Model):
    nombre_libre = CharField(max_length=60)
    estudiante = ForeignKey(Estudiante)
    docente = ForeignKey(Docente)
    persona_registrada = ForeignKey(PersonaExterna)

class SolicitudDeDocumentoPublicado(models.Model):
    quien = ForeignKey(QuienSolicitaDocumento)
    documento_solicitado = ForeignKey(Documento)
    texto_fundamento = TextField()
    fecha_solicitud = DateTimeField(auto_now=False, auto_now_add=True)

class FeedbacksDeLectura(models.Model):
    quien = ForeignKey(QuienSolicitaDocumento)
    texto_feedback = TextField()

class BusquedasLibres(models.Model):
    quien = ForeignKey(QuienSolicitaDocumento)
    texto_buscado = TextField()

    class Meta:
        verbose_name_plural = u'Búsquedas libres'

class ResultadosDeBusqueda(models.Model):
    busqueda = TextField()
    documentos = ManyToManyField(Documento)



#class BaseCurso(models.Model):
#    nombre = CharField(max_length=60)
#    codigo = CharField(max_length=6)
#    obs = TextField()
#    plan = ForeignKey(Plan)
#    fecha_alta = DateTimeField(auto_now=False, auto_now_add=True)
#
#    class Meta:
#        verbose_name_plural = u'Los cursos de un plan'

#class Curso(models.Model):
#    curso = ForeignKey(BaseCurso)
#    generacion = ForeignKey(Generacion)
#    obs = TextField()
#    fecha_alta = DateTimeField(auto_now=False, auto_now_add=True)
#
#    class Meta:
#        verbose_name_plural = u' Los cursos de cada generación específica'

#class DocenteCurso(models.Model):
#    docente = ForeignKey(Docente)
#    curso = ForeignKey(Curso)
#
#    class Meta:
#        verbose_name_plural = u'Pertenencia de un docente a un curso'

#class EstudianteCurso(models.Model):
#    estudiante = ForeignKey(Estudiante)
#    curso = ForeignKey(Curso)
#
#    class Meta:
#        verbose_name_plural = u'Pertenencia de un estudiante a un curso'
