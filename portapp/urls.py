# coding: utf-8
#       (C) 2011 by Jorge Chávez, Paribanú Freitas & Haroldo Stenger (UDELAR, Facultad de Psicología)
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

from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, RedirectView, CreateView
from porta.portapp.views import *
from porta.portapp.models import *
from porta.portapp.globales import   AVATARS,\
                            MENU_PUBLICO,\
                            MENU_ESTUDIANTE,\
                            MENU_DOCENTE,\
                            MENU_USUARIO,\
                            MENU_ADMINISTRADOR

urlpatterns = patterns('',
    (r'^$', MenuPublicoTemplateView.as_view()), 
                       
    (r'^registrarse_como_usuario/$', 
            'portapp.views.registrar_usuario'), 
    
    (r'^registrarse_como_docente/$', 
            'portapp.views.registrar_docente'), 
    
    (r'^registrarse_como_estudiante/$', 
            'portapp.views.registrar_estudiante'), 
    
    url(r'^login/$', 
            'portapp.views.my_login', 
            name='my_login'), 
    
    url(r'^logout/$', 
            'portapp.views.my_logout', 
            name='my_logout'), 

    (r'^inicia/$', 
        login_required(
                    UserTypeDependRedirectView.as_view(), 
                    login_url='/porta/portapp/login/'
        )
    ), 
        
    (r'^inicia_avatars/$', 
        login_required(
                    AvatarListView.as_view(
                            template_name='inicia.html'
                    ), 
                    login_url='/porta/portapp/login/'
        )
    ), 
        
    (r'^docentes/$',
        login_required(
                ExtraContextListView.as_view(
                    queryset=Docente.objects.all().order_by('apellido', 'nombre'), 
                    template_name='lista.html' 
                ), 
                login_url='/porta/portapp/login/'
        )
    ), 
            
    (r'^estudiantes/$', 
        login_required(
                ExtraContextListView.as_view(
                    queryset=Estudiante.objects.all().order_by('apellido', 'nombre'), 
                    template_name='lista.html'
                ), 
                login_url='/porta/portapp/login/'
        )
    ),     

    url(r'^estudiante_crear_coautoria/$', 
        login_required(
                CoautoriaEstudianteCreateView.as_view(
                    form_class=CoautoriaModelForm,             
                    template_name='createmodel.html'
                ), 
                login_url='/porta/portapp/login/'
        ), 
        name='estudiante_crear_coautoria'
    ), 

##    url(r'^estudiante_crear_coautoria_estudiante/(?P<coautoria_param>\d+)/$', 
##        login_required(
##                CoautoriaEstudianteCreateView.as_view(
##                    form_class=CoautoriaEstudianteModelForm, 
##                    template_name='createmodel_coautoria_estudiante.html'
##                ), 
##                login_url='/porta/portapp/login/'
##        ), 
##        name='estudiante_crear_coautoria_estudiante'
##    ), 

    (r'^ingresar_documento', 
        'portapp.views.ingresar_documento'), 
    
    (r'^ver_co_autorias_de_las_que_uno_participa/$', 
        login_required(
                CoautoriasDeUnoListView.as_view(
                    template_name='ver_co_autorias_de_las_que_uno_participa.html'
                ), 
                login_url='/porta/portapp/login/')
    ), 

    (r'^ver_documentos_de_los_que_uno_participa/$', 
        login_required(
                DocumentosDeUnoListView.as_view(
                    template_name='ver_documentos_de_los_que_uno_participa.html'
                ), 
                login_url='/porta/portapp/login/')
    ), 

    (r'^agregar_estudiantes/$', 
        login_required(
                AgregarEstudianteListView.as_view(
                    template_name='agregar_estudiante_a_coautoria.html'
                ), 
                login_url='/porta/portapp/login/')
    ), 

    (r'^agregar_estudiante/(?P<coautoria_param>\d+)/$', 
        login_required(
                AgregarEstudianteCoautoriaSeleccionadaCreateView.as_view(
                    template_name='agregar_estudiante.html', 
                    form_class=CoautoriaEstudianteModelForm
                ), 
                login_url='/porta/portapp/login/')
    ), 

    (r'^validar_propuestas/$', 
        login_required(
                ValidarEstudianteCoautoriaSeleccionadaCreateView.as_view(
                    template_name='validar_propuestas.html'
                ), 
                login_url='/porta/portapp/login/')
    ),

    (r'^agregarse_uno_a_coautoria/$', 
        login_required(
                AgregarseUnoACoautoriaSeleccionadaCreateView.as_view(
                    template_name='agregarse_a_coautoria.html', 
                    form_class=CoautoriaEstudianteModelForm
                ), 
                login_url='/porta/portapp/login/'
        )
    ), 



) ##último paréntesis de urlpatterns
