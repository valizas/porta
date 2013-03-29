# coding: utf-8

AVATARS=['estudiante', 'docente', 'usuario', 'administrador']

MENU_PUBLICO=\
u"""registrarse por primera vez como estudiante|/porta/portapp/registrarse_como_estudiante/
registrarse por primera vez como docente|/porta/portapp/registrarse_como_docente/
registrarse por primera vez como usuario externo|/porta/portapp/registrarse_como_usuario/
ingresar al sistema|/porta/portapp/inicia/"""

### idea futura (2/12/2011): que para ser estudiante, o docente, otro te vea en una lista de solicitudes y te valide 
### y quede registrado que tu validador es tal
### para minimizar el trabajo "administrativo" y también minimizar los abusos

MENU_ESTUDIANTE=\
u"""|
ESTUDIANTE|
|
crear una co-autoría de la cual uno será miembro|/porta/portapp/estudiante_crear_coautoria/
agregar otro estudiante a una co-autoría a la cual uno ya pertenece|/porta/portapp/agregar_estudiantes/
validar membresías que han sido propuestas a coautorías|/porta/portapp/validar_propuestas/
agregarse uno como miembro de una co-autoría existente|/porta/portapp/agregarse_uno_a_coautoria/
|
ingresar/subir documento para archivo y adjudicación de autoría|/porta/portapp/ingresar_documento/
adjudicar una co-autoría existente a un documento existente|.
adjudicar autoría individual a un documento existente|.
|
ver documentos de los que uno participa como autor o co-autor|/porta/portapp/ver_documentos_de_los_que_uno_participa/
ver co-autorías de las que uno participa como autor o co-autor|/porta/portapp/ver_co_autorias_de_las_que_uno_participa/
ver notificaciones|.
lista de docentes registrados en el Sistema|/porta/portapp/docentes/"""

MENU_DOCENTE=\
u"""|
DOCENTE|
|
crear una co-autoría estudiantil|/porta/portapp/docente_crear_coautoría/
ver documentos de los que uno participa como docente referente|/porta/portapp/
validar haber sido propuesto como docente referente de un documento|/porta/portapp/validar_haber_sido_propuesto/"""

MENU_USUARIO=\
u"""|
USUARIO|
|
realizar una búsqueda|.
ver estado de las solicitudes de documentos|."""

MENU_ADMINISTRADOR=\
u"""|
ADMINISTRADOR|
|
acceder a la Administración del Sistema|/admin/"""

