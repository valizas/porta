#  coding: utf-8
from django import forms
from django.db.models import Q
import porta.portapp.models as models

class Login(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.widgets.PasswordInput())

class DocumentoForm(forms.Form):
    titulo = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'style':'width:600px'}))
    fecha_creacion = forms.DateField(widget=forms.TextInput(attrs={'size':'12'}))
    keywords = forms.CharField(widget=forms.Textarea(attrs={'style':'width:600px;height:50px'}))
    abstract = forms.CharField(widget=forms.Textarea(attrs={'style':'width:600px'}))
    documento = forms.FileField()

    def __init__(self, *args,  **kwargs):
        super(DocumentoForm, self).__init__(*args,  **kwargs)
        self.fields['docente_referente'] = forms.ChoiceField(choices=[(0,'Elegir un docente')]+
            [ (d.id, "%s %s"%(d.nombre,  d.apellido)) 
                for d in models.Docente.objects.all().order_by('apellido', 'nombre') ])

class Buscar(forms.Form):
    buscar=forms.CharField(min_length=3)

class AvatarUser(forms.Form):
    def __init__(self):
        super(AvatarUser, self).__init__(*args, **kwargs)
        choices=[s for s in kwargs.keys() if s in AVATARS]
        self.avatar=forms.ChoiceField(choices=choices)

class CoautoriaModelForm(forms.ModelForm):
    
    class Meta:
        model=models.Coautoria

class CoautoriaEstudianteModelForm(forms.ModelForm):

    class Meta:
        model=models.CoautoriaEstudiante
        exclude = ('fecha_ingreso','fecha_verificado')        

class SeleccionarForm(forms.Form):
    ape_ini=forms.CharField(required=False,  label=u"El apellido comienza con")
    nom_ini=forms.CharField(required=False,  label=u"El nombre comienza con")
    letras_like=forms.CharField(required=False,  label=u"El nombre o el apellido contienen")
    current_group=forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        ape_ini = None
        nom_ini = None
        letras_like = None

        if kwargs.has_key('initial'):
            ape_ini = kwargs['initial'].get('ape_ini', '').upper()
            nom_ini = kwargs['initial'].get('nom_ini', '').upper()
            letras_like = kwargs['initial'].get('letras_like', '').upper()
            current_group=kwargs['initial'].get('current_group', None)

        m=kwargs['m']
        del(kwargs['m'])
        grupo=kwargs.get('grupo', None)
        if grupo is not None:
            del(kwargs['grupo'])

        super(SeleccionarForm, self).__init__(*args, **kwargs)

        if ape_ini or nom_ini or letras_like:
            group_max=10
            q=m.objects.all().order_by('apellido', 'nombre')
            if ape_ini:
                q=q.filter(apellido__gte=ape_ini, apellido__lt=''.join([ape_ini, 'Z'*50])[:50])
            if nom_ini:
                q=q.filter(nombre__gte=nom_ini, nombre__lt=''.join([nom_ini, 'Z'*50])[:50])
            if letras_like:
                q=q.filter(Q(nombre__contains=letras_like.upper()) | Q(apellido__contains=letras_like.upper()))

            how_many=q.count()
            size_group=how_many // group_max + 1 if how_many % group_max else 0

            if size_group <= 1:
                self.fields['opciones']=forms.ChoiceField(
                        required=False,
                        choices= [(p.id, "%s (%s de %s)" % (p.__unicode__(), n+1, how_many) )for n, p in enumerate(q) ], 
                        widget=forms.widgets.Select(attrs={'type':'submit'}))
            else:
                show_group = int(current_group)
                
                choices=[]
                if show_group > 1:
                    choices.extend([('<- Grupo anterior',  u"<- Grupo anterior")])
                choices.extend( [(p.id,
                                              "%s (%s de %s)" % (p.__unicode__(),
                                              1+n+(show_group-1) * group_max, how_many) )
                        for n, p in enumerate(q[(show_group-1) * group_max:(show_group) * group_max ]) ] )
                if show_group < size_group:
                    choices.extend( [('Siguiente grupo ->',  u"Siguiente grupo ->")] )
                self.fields['opciones']=forms.ChoiceField(
                        required=False,
                        choices=choices,
##                        widget=forms.widgets.Select(attrs={'type':'submit'}))
                        widget=forms.widgets.Select())

class SeleccionarCoautoriaForm(forms.Form):
    seudonimo_ini=forms.CharField(required=False,  label=u"El seudónimo comienza con")
    letras_like=forms.CharField(required=False, label=u"El seudónimo contiene")
    current_group=forms.IntegerField(widget=forms.HiddenInput)
    
    def __init__(self, *args, **kwargs):
        seudonimo_ini = None
        letras_like = None

        if kwargs.has_key('initial'):
            seudonimo_ini = kwargs['initial'].get('seudonimo_ini', '').upper()
            letras_like = kwargs['initial'].get('letras_like', '').upper()
            current_group=kwargs['initial'].get('current_group', None)

        m=kwargs['m']
        del(kwargs['m'])
        grupo=kwargs.get('grupo', None)
        if grupo is not None:
            del(kwargs['grupo'])

        super(SeleccionarCoautoriaForm, self).__init__(*args, **kwargs)

        if seudonimo_ini or letras_like:
            print seudonimo_ini
            group_max=5
            q=m.objects.all().order_by('seudonimo')
            if seudonimo_ini:
                q=q.filter(seudonimo__gte=seudonimo_ini, seudonimo__lt=''.join([seudonimo_ini, 'Z'*50])[:50])
            if letras_like:
                q=q.filter(seudonimo__contains=letras_like.upper())

            how_many=q.count()
            size_group=how_many // group_max + 1 if how_many % group_max else 0

            if size_group <= 1:
                self.fields['opciones']=forms.ChoiceField(
                        required=False,
                        choices= [(p.id, "%s (%s de %s)" % (p.__unicode__(), n+1, how_many) )for n, p in enumerate(q) ], 
                        widget=forms.widgets.Select(attrs={'type':'submit'}))
            else:
                show_group = int(current_group)
                
                choices=[]
                if show_group > 1:
                    choices.extend([('<- Grupo anterior',  u"<- Grupo anterior")])
                choices.extend( [(p.id,
                                              "%s (%s de %s)" % (p.__unicode__(),
                                              1+n+(show_group-1) * group_max, how_many) )
                        for n, p in enumerate(q[(show_group-1) * group_max:(show_group) * group_max ]) ] )
                if show_group < size_group:
                    choices.extend( [('Siguiente grupo ->',  u"Siguiente grupo ->")] )
                self.fields['opciones']=forms.ChoiceField(
                        required=False,
                        choices=choices,
##                        widget=forms.widgets.Select(attrs={'type':'submit'}))
                        widget=forms.widgets.Select())

class ValidarPropuestasForm(forms.Form):
    clave= forms.IntegerField(widget=forms.HiddenInput)
    estudiante = forms.IntegerField(widget=forms.HiddenInput)
    coautoria = forms.IntegerField(widget=forms.HiddenInput)
    validar = forms.BooleanField(required=False)
##    def __init__(self, *args, **kwargs):
##        super(ValidarPropuestasForm, self).__init__(*args, **kwargs)
##        self.fields['validar'].initial=True

