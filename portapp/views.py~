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

import re
import os
from models import *
from django.db.models import Q
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, RequestContext 
from django import forms
from datetime import datetime
from django.conf import settings
from django.core.files import File
from django.utils.encoding import force_unicode
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, RedirectView,  TemplateView,  CreateView
from porta.portapp.forms import *
from porta.portapp.globales import   AVATARS,\
                            MENU_PUBLICO,\
                            MENU_ESTUDIANTE,\
                            MENU_DOCENTE,\
                            MENU_USUARIO,\
                            MENU_ADMINISTRADOR

class MenuPublicoTemplateView(TemplateView):
    
    template_name='menu_publico.html'
    
    def render_to_response(self, context, **response_kwargs):
        rc=super(MenuPublicoTemplateView, self).render_to_response(context, **response_kwargs)
        rc.context_data['object_list']=[y.split('|') for y in MENU_PUBLICO.split('\n')]
        return rc
        

def determine_user_type(r): #####  if user.is_active:
    roles=[]
    u=r.user

    if u.is_staff:
        roles.append("administrador")

    try:
        Estudiante.objects.get(user__exact=u)
        roles.append("estudiante")
    except Estudiante.DoesNotExist:
        pass

    try:
        Docente.objects.get(user__exact=u)
        roles.append("docente")
    except Docente.DoesNotExist:
        pass

    roles.append("usuario")

    return roles

def get_valid_filename(s):
    s = force_unicode(s).strip().replace(' ', '_')
    return re.sub(r'[^-A-Za-z0-9_.]', '', s)

### este es el único view que no lleva @login_required
def my_login(request):
    if request.POST:
        l=Login(request.POST)
        if l.is_valid():
            user = authenticate(username=l.cleaned_data['username'], password=l.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/porta/portapp/inicia/')
                else:
                    # su cuenta no está activa
                    return HttpResponseRedirect('/porta/portapp/login/')
            else:
                return HttpResponseRedirect('/porta/portapp/login/')
    else:
        l=Login()
        return render_to_response('login.html', {'form':l}, RequestContext(request))

@login_required(login_url='/porta/portapp/login/')
def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/porta/portapp/')

@login_required(login_url='/porta/portapp/login/')
def ingresar_documento(request, co_autorado=False):

#   la definición se hace para cada ejecución del view para que se actualice la lista de docentes disponibles
#   aunque para el método POST no es del todo necesario recrearla con la lista de docentes, 
#   a menos que el método falle y tenga que reenviar el form.

    if request.method=='POST':
        docu=DocumentoForm(request.POST, request.FILES)
        if docu.is_valid():
            dr=docu.cleaned_data
            dr['docente_referente']=Docente.objects.get(pk=int(dr['docente_referente']))
            filename_original=request.FILES['documento'].name
            filename_sanitizado=get_valid_filename(filename_original)
            del dr['documento']
            docum=Documento(**dr)
            # grabar el archivo
            upload_dir = \
                'upload/'
                #date.today().strftime(settings.UPLOAD_PATH)
            docum.path = os.path.join(upload_dir, filename_sanitizado)
            dest = \
                open(docum.path, 'wb')
            dest.write(request.FILES['documento'].read())
            dest.close()
            docum.save()
            DocumentoEstudiante.objects.create(
                   documento=docum, 
                   estudiante=Estudiante.objects.get(user=request.user))
            docu=DocumentoForm()
            return render_to_response('ingresar_documento.html', {'docu':docu}, context_instance=RequestContext(request))
        else:
            return render_to_response('ingresar_documento.html', {'tarea':'Ingreso de documento co-autorado','docu':docu}, context_instance=RequestContext(request))
    else:
        docu=DocumentoForm()
        return render_to_response('ingresar_documento.html', {'docu':docu}, context_instance=RequestContext(request))

def registrar_estudiante(request):
    pass
    
def registrar_docente(request):
    pass

def registrar_persona_externa(request):
    pass

def registrar_usuario(request):
    pass

##@login_required(login_url='/porta/portapp/login/')
##def agregar_estudiantes(request, documento=None):
##
##    class EstudianteForm(forms.Form):
##        ##documento_id=forms.IntegerField(widget=HiddenInput())
##        def __init__(self, documento=None, *args, **kwargs):
##            super(forms.Form, self).__init__(*args, **kwargs)
##            self.fields['estudiante'] = forms.ChoiceField(choices=[(x.id, x) for x in Estudiante.objects.all().order_by('apellido', 'nombre')])
##            self.fields['documento'] = forms.ChoiceField(choices=[(documento.id, documento.titulo)])
##
##    if request.method=='POST':
##        try:
##            e=Estudiante.objects.get(id=int(request.POST['estudiante']))
##        except:
####            docnum=int(request.POST['documento'])
##            docnum=int(documento)
##            ef=EstudianteForm(documento=Documento.objects.get(pk=docnum))
##            return render_to_response('agregar_estudiantes.html', {'ef':ef}, context_instance=RequestContext(request))
####        d=Documento.objects.get(id=int(request.POST['documento']))
##        d=Documento.objects.get(id=int(documento))
##        DocumentoEstudiante.objects.create(documento=d, estudiante=e)
##        return HttpResponseRedirect('/porta/portapp/agregar_estudiantes/%s'%(int(request.POST['documento']), ))
##    else:
##        docnum=int(documento)
##        ef=EstudianteForm(documento=Documento.objects.get(pk=docnum))
##        return render_to_response('agregar_estudiantes.html', {'ef':ef, 'action':'/porta/portapp/agregar_estudiantes/%s'%(documento,)}, context_instance=RequestContext(request))

@login_required(login_url='/porta/portapp/login/')
def quitar_estudiantes(request):
    if request.method=='POST':
        ef=EstudianteForm(request)
        if ef.is_valid():
            e=ef.clean_data['estudiante']
            d=ef.clean_data['documento']
            DocumentoEstudiante.objects.delete(documento=d, estudiante=e)
            return HttpResponseRedirect(reverse_urls('menu'))
        else:
            ef=EstudianteForm()
            return render_to_response('quitar_estudiantes', {'ef':ef})
    else:
        ef=EstudianteForm()
        return render_to_response('quitar_estudiantes', {'ef':ef})

@login_required(login_url='/porta/portapp/login/')
def cambiar_docente_referente(request):
    if request.method=='POST':
        pass
    else:
        return render_to_response('cambiar_docente_referente', {'':0})

@login_required(login_url='/porta/portapp/login/')
def ver_solicitudes_a_mi(request):
    if request.method=='POST':
        pass
    else:
        return render_to_response('ver_solicitudes_a_mi', {'':0})

@login_required(login_url='/porta/portapp/login/')
def denegar_solicitud(request):
    if request.method=='POST':
        pass
    else:
        return render_to_response('denegar_solicitud', {'':0})

@login_required(login_url='/porta/portapp/login/')
def buscar(request):
    if request.method=='POST':
        pass
    else:
        return render_to_response('buscar', {'':0})

@login_required(login_url='/porta/portapp/login/')
def solicitar(request):
    if request.method=='POST':
        pass
    else:
        return render_to_response('solicitar', {'':0})

@login_required(login_url='/porta/portapp/login/')
def dar_feedback(request):
    if request.method=='POST':
        pass
    else:
        return render_to_response('dar_feedback', {'':0})

@login_required(login_url='/porta/portapp/login/')
def ver_estudiantes(request):
    if request.method=='POST':
        pass
    else:
        return {'docentes': Estudiante.objects.all().order_by('apellido', 'nombre')}

### BAD CODE
##@login_required(login_url='/porta/portapp/login/')
##def estudiante_crear_coautoria_estudiante(request, coautoria_param=None):
##    CreateView.as_view(
##            model=CoautoriaEstudiante,
##            success_url="/estudiante_crear_coautoria_estudiante/%(coautoria_param)s/",
##            template_name='createmodel_coautoria_estudiante.html')


class ExtraContextListView(ListView):
    
    def get_context_data(self, **kwargs):
        context=super(ExtraContextListView, self).get_context_data(**kwargs)
        context['root_path']='/porta/portapp/'
        context['menu']=u'Menú del %s' % (determine_user_type(self.request)[0], )
        context['quien']=u'Identificado: %s:' % (', '.join(determine_user_type(self.request)), )
        context.update({(k, kwargs[k]) for k in kwargs.keys() if k.startswith('data_')})

        return context
        
        #context['logout_url']=None
        
class ExtraContextCreateView(CreateView):

    def get_success_url(self):

#        return "/porta/portapp/estudiante_crear_coautoria_estudiante/%(coautoria)s/" \
#            % {'coautoria':self.object.pk}
        pass
        return "/porta/portapp/inicia"

    def get_context_data(self, **kwargs):
        context=super(ExtraContextCreateView, self).get_context_data(**kwargs)
        context['root_path']='/porta/portapp/'

        return context
        
class AvatarListView(ListView):

    def get_context_data(self, **kwargs):
        context=super(AvatarListView, self).get_context_data(**kwargs)
        context['root_path']='/porta/portapp/'
        context['menu']=u'Menú del %s:' % (', '.join(determine_user_type(self.request)), )
        if 'estudiante' in determine_user_type(self.request):
            context['nombre_completo']=Estudiante.objects.get(user=self.request.user)
        elif 'docente' in determine_user_type(self.request):
            context['nombre_completo']=Docente.objects.get(user=self.request.user)
        elif 'usuario' in determine_user_type(self.request):
            context['nombre_completo']=PersonaExterna.objects.get(user=self.request.user)

        return context

        #context['logout_url']=None

    def get_queryset(self, **kwargs):
        MENU_AVATAR=[]
        roles=determine_user_type(self.request)
        if 'administrador' in roles:
            MENU_AVATAR.extend([y.split('|') for y in MENU_ADMINISTRADOR.split('\n')])
        if 'estudiante' in roles:
            MENU_AVATAR.extend([y.split('|') for y in MENU_ESTUDIANTE.split('\n')])
        if 'docente' in roles:
            MENU_AVATAR.extend([y.split('|') for y in MENU_DOCENTE.split('\n')])
        if 'usuario' in roles:
            MENU_AVATAR.extend([y.split('|') for y in MENU_USUARIO.split('\n')])
        return MENU_AVATAR


class UserTypeDependRedirectView(RedirectView):
    def get_redirect_url(self, **kwargs):
        if False:
            return( "/porta/portapp/inicia_%s/" % (determine_user_type(self.request), ))
        else:
            return( "/porta/portapp/inicia_avatars/")


class CoautoriaEstudianteCreateView(CreateView):
    def render_to_response(self, context):
        context.update({'coautoria_param':self.kwargs.get('coautoria_param', None)})
        return super(CoautoriaEstudianteCreateView, self).render_to_response(context)

    def get_success_url(self):

        return "/porta/portapp/inicia"

    def form_valid(self,  form):
        response=super(CoautoriaEstudianteCreateView, self).form_valid(form)
        estudiante = Estudiante.objects.get(user=self.request.user)
        
        CoautoriaEstudiante.objects.create(
            estudiante = estudiante, 
            coautoria = self.object, 
            stage = 'CREADOR')
        return response

class CoautoriasDeUnoListView(ListView):

    def get_queryset(self, **kwargs):
        estudiante = Estudiante.objects.get(user=self.request.user)
        coautorias_de_uno=sorted([ce.coautoria 
                        for ce in CoautoriaEstudiante.objects.filter(estudiante=estudiante)], 
                key=lambda co:co.fecha_alta, reverse=True)
                
        queryset=[
                            (
                            (cou, cou.fecha_alta), 
                                 [ (ce.estudiante, ce.stage) for ce in cou.coautoriaestudiante_set.all() ]
                           ) for cou in coautorias_de_uno
                           ]

        return queryset
        
    def get_context_data(self, **kwargs):
        context=super(CoautoriasDeUnoListView, self).get_context_data(**kwargs)
        context['root_path']='/porta/portapp/'

        return context

class DocumentosDeUnoListView(ListView):

    def get_queryset(self, **kwargs):
        estudiante = Estudiante.objects.get(user=self.request.user)

        queryset_individuales= [ (de.documento, 
                                  de.documento.fecha_creacion, 
                                  de.documento.asignatura.descripcion if de.documento.asignatura else "---"
                                  ) for de in estudiante.documentoestudiante_set.all()]
        
        coautorias_de_uno=sorted([ce.coautoria
                        for ce in CoautoriaEstudiante.objects.filter(estudiante=estudiante)], 
                key=lambda co:co.fecha_alta, reverse=True)
              
        a = [cou.coautoriaestudiante_set.get(estudiante=estudiante) for cou in coautorias_de_uno]

        
        queryset_coautorias= []
        for x in a:
                y=x.coautoria.documentocoautoria_set.all()
                
                queryset_coautorias.extend( [ (yy.documento.titulo, 
                                                yy.documento.fecha_creacion,
                                                yy.coautoria, 
                                                 yy.documento.asignatura.descripcion if yy.documento.asignatura else "---") for yy in y] )

        queryset={'individuales':queryset_individuales, 
                            'coautorias':queryset_coautorias}

        return queryset

    def get_context_data(self, **kwargs):
        context=super(DocumentosDeUnoListView, self).get_context_data(**kwargs)
        context['root_path']='/porta/portapp/'

        return context

class AgregarEstudianteListView(ListView):

    def get_context_data(self, **kwargs):
        context=super(AgregarEstudianteListView, self).get_context_data(**kwargs)
        context['root_path']='/porta/portapp/'
        context['titulo']=u"Haga click en el seudónimo de la coautoría"\
                                             " a la que desea agregar un estudiante:"
        return context

    def get_queryset(self, **kwargs):
        estudiante = Estudiante.objects.get(user=self.request.user)
        queryset=["<a href='/porta/portapp/agregar_estudiante/%s'>%s</a>" 
                                    % (c.coautoria.pk, c.coautoria , )
                  for c in CoautoriaEstudiante.objects.filter(estudiante=estudiante)]
        return queryset


class AgregarEstudianteCoautoriaSeleccionadaCreateView(CreateView):
    
    def get_form_kwargs(self):
        kwargs = super(AgregarEstudianteCoautoriaSeleccionadaCreateView, self).get_form_kwargs()
        if self.request.method=='POST':
            coautoria_param = self.kwargs.get('coautoria_param')
            
            opcion_estudiante = self.request.POST.get('opciones', None)
            if opcion_estudiante is not None:
                try:
                    estudiante_pk = int(opcion_estudiante)
                except:
                    return kwargs
                kwargs.update({'data':{'estudiante':estudiante_pk, 
                                                        'coautoria':coautoria_param, 
                                                        'stage':'PROPUESTO'}})
        print kwargs
        return kwargs

    def get_context_data(self, **kwargs):
        context=super(AgregarEstudianteCoautoriaSeleccionadaCreateView, self).get_context_data(**kwargs)
        if self.request.method=='GET':
            sf=SeleccionarForm(m=Estudiante)
        else:
            opcion_estudiante = self.request.POST.get('opciones', None)
            grupo=0
            if opcion_estudiante == '<- Grupo anterior':
                grupo=-1
            elif opcion_estudiante == 'Siguiente grupo ->':
                grupo=+1
            post_dict=self.request.POST.copy()
            try:
                current_group = int(post_dict['current_group'])
            except ValueError:
                current_group =1
            if current_group < 1:
                current_group = 1
            post_dict.update({'current_group':current_group+grupo})
            sf=SeleccionarForm(initial=post_dict, m=Estudiante, grupo=grupo)
        coautoria_param = self.kwargs.get('coautoria_param')
        coautoria=Coautoria.objects.get(pk=int(coautoria_param))
        context.update({
            'estudiantes_ya_pertenecientes': 
                    [ce.estudiante for ce in CoautoriaEstudiante.objects.filter(coautoria=coautoria_param) ], 
            'titulo': u"Agregar a la coautoría %s " % (coautoria, ), 
            'coautoria_param': coautoria_param, 
            'sf':sf})
        return context

#    def render_to_response(self, context):
#        if self.request.method == 'GET':
#            sf=SeleccionarForm(m=Estudiante)
#            coautoria_param = self.kwargs.get('coautoria_param')
#            coautoria=Coautoria.objects.get(pk=int(coautoria_param))
#            context.update({
#                'titulo': u"Agregar a la coautoría %s " % (coautoria, ), 
#                'coautoria_param': coautoria_param, 
#                'sf':sf
#                })
#        else:
#            if self.request.POST['opciones'] == '<- Grupo anterior':
#                grupo=-1
#            elif self.request.POST['opciones'] == 'Siguiente grupo ->':
#                grupo=+1
#            else:
#                self.form_valid()
#            sf=SeleccionarForm(initial=self.request.POST, m=Estudiante, grupo=grupo)
#            coautoria_param = self.kwargs.get('coautoria_param')
#            coautoria=Coautoria.objects.get(pk=int(coautoria_param))
#            context.update({
#                'titulo': u"Agregar a la coautoría %s " % (coautoria, ), 
#                'coautoria_param': coautoria_param, 
#                'sf':sf
#                })
#        return super(AgregarEstudianteCoautoriaSeleccionadaCreateView, self).render_to_response(context)



#    def post(self, request, *args, **kwargs):
#        opcion_estudiante = request.POST.get('opciones', None)
#        if opcion_estudiante:
#            coautoria_param = self.kwargs.get('coautoria_param')
#            coautoria=Coautoria.objects.get(pk=int(coautoria_param))
#            estudiante=Estudiante.objects.get(pk=int(opcion_estudiante))
#            self.object=CoautoriaEstudianteModelForm(
#                    estudiante=estudiante, 
#                    coautoria=coautoria, 
#                    stage='PROPUESTO'
#                    )
#            return super(AgregarEstudianteCoautoriaSeleccionadaCreateView, self).post(self, request, *args, **kwargs)
#        return super(AgregarEstudianteCoautoriaSeleccionadaCreateView, self).post(self, request, *args, **kwargs)

    def get_success_url(self):
        return "/porta/portapp/inicia"


class AgregarseUnoACoautoriaSeleccionadaCreateView(CreateView):

    def get_form_kwargs(self):
        kwargs = super(AgregarseUnoACoautoriaSeleccionadaCreateView, self).get_form_kwargs()
        if self.request.method=='POST':            
            opcion_coautoria = self.request.POST.get('opciones', None)
            if opcion_coautoria is not None:
                try:
                    coautoria_pk = int(opcion_coautoria)
                except:
                    return kwargs
                kwargs.update({'data':{'estudiante':Estudiante.objects.get(user=self.request.user).pk, 
                                                        'coautoria':opcion_coautoria, 
                                                        'stage':'AUTO-PROPUESTO'}})
        return kwargs
        
    def post(self, request, *args, **kwargs):
        self.object = None
        from django.views.generic.edit import BaseCreateView
        r= super(BaseCreateView, self).post(request, *args, **kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        print form.is_bound
        print form.is_valid()
        print form.errors
        return r
        
    def get_context_data(self, **kwargs):
        context=super(AgregarseUnoACoautoriaSeleccionadaCreateView, self).get_context_data(**kwargs)
        if self.request.method=='GET':
            sf=SeleccionarCoautoriaForm(m=Coautoria)
            context.update({
    #            'estudiantes_ya_pertenecientes': 
    #                    [ce.estudiante for ce in CoautoriaEstudiante.objects.filter(coautoria=opcion_coautoria) ], 
                'sf':sf})
        else:
            opcion_coautoria = self.request.POST.get('opciones', None)
            grupo=0
            if opcion_coautoria == '<- Grupo anterior':
                grupo=-1
            elif opcion_coautoria == 'Siguiente grupo ->':
                grupo=+1
            post_dict=self.request.POST.copy()
            try:
                current_group = int(post_dict['current_group'])
            except ValueError:
                current_group =1
            if current_group < 1:
                current_group = 1
            post_dict.update({'current_group':current_group+grupo})
            sf=SeleccionarCoautoriaForm(initial=post_dict, m=Coautoria, grupo=grupo)
            try:
                coautoria=Coautoria.objects.get(pk=int(opcion_coautoria))

                context.update({
        #           'estudiantes_ya_pertenecientes': 
        #                    [ce.estudiante for ce in CoautoriaEstudiante.objects.filter(coautoria=opcion_coautoria) ], 
                    'titulo': u"Agregarse uno a la coautoría %s " % (coautoria, )})
            except:
                pass
                
            context.update({
    #            'estudiantes_ya_pertenecientes': 
    #                    [ce.estudiante for ce in CoautoriaEstudiante.objects.filter(coautoria=opcion_coautoria) ], 
                'sf':sf})
        return context

    def get_success_url(self):
        return "/porta/portapp/inicia"


class ValidarEstudianteCoautoriaSeleccionadaCreateView(CreateView):
    form_class=ValidarPropuestasForm

    def get(self, request, *args, **kwargs):
        self.object=None
        r=self.get_context_data()
        if r['object_list']:
            return self.render_to_response(r)
        else:
            return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        context=super(ValidarEstudianteCoautoriaSeleccionadaCreateView, self).get_context_data(**kwargs)
        context['root_path']='/porta/portapp/'
        context['titulo']=u"Haga click en las propuestas de membresía que desea validar:"

        # Encontrar coautorías propuestas
        estudiante = Estudiante.objects.get(user=self.request.user)
        ce_uno=CoautoriaEstudiante.objects\
                        .filter(estudiante=estudiante)\
                        .filter(stage='PROPUESTO')
        coautorias_de_uno_ok = Estudiante.objects.get(user=self.request.user)\
            .coautoriaestudiante_set.filter((Q(stage='CREADOR')| Q(stage='VERIFICADO')))
        validar_propuestas = [cduok.coautoria.coautoriaestudiante_set\
            .exclude(estudiante=estudiante)\
            .filter(Q(stage='AUTO-PROPUESTO')| Q(stage='PROPUESTO')) 
                for cduok in coautorias_de_uno_ok]

        ce_propuestas=list(ce_uno)
        for v in validar_propuestas:
            for vv in v:
                ce_propuestas.append(vv)
        validar_propuestas_FormSet = formset_factory(ValidarPropuestasForm)
        context['object_list']=None

        ValidarPropuestasFormSet=validar_propuestas_FormSet(initial=
                [{'clave':ce.pk, 
                    'estudiante':ce.estudiante.pk, 
                   'coautoria':ce.coautoria.pk, 
                   'validar':True} for ce in ce_propuestas])
        propuestas=[(x, ValidarPropuestasFormSet[n]) for n, x in enumerate(ce_propuestas)]
        context['object_list']=propuestas
        context['management_form']=ValidarPropuestasFormSet.management_form

        return context

#    def form_invalid(self):
#        r=self.get_context_data()
#        if r['object_list']:
#            return self.render_to_response(r)
#        else:
#            return HttpResponseRedirect(self.get_success_url())


    def post(self, request, *args, **kwargs):
        self.object=None
        validar_propuestas_FormSet = formset_factory(ValidarPropuestasForm)
        ValidarPropuestasFormSet=validar_propuestas_FormSet(self.request.POST)
        ValidarPropuestasFormSet.is_valid()
        for x in ValidarPropuestasFormSet.cleaned_data:
            if x and x['validar']:
                ce=CoautoriaEstudiante.objects.get(pk=x['clave'])
                ce.stage='VERIFICADO'
                ce.save()
        r=self.get_context_data()
        if r['object_list']:
            return self.render_to_response(r)
        else:
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return "/porta/portapp/inicia"

#commented out from:  class AgregarEstudianteCoautoriaSeleccionadaCreateView(CreateView):

#    def post(self, request, *args, **kwargs):
#        self.object = None
#        from django.views.generic.edit import BaseCreateView
#        r= super(BaseCreateView, self).post(request, *args, **kwargs)
#        form_class = self.get_form_class()
#        form = self.get_form(form_class)
#        print form.is_bound
#        print form.is_valid()
#        print form.errors
#        return r
 
