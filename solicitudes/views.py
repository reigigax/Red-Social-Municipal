from django.shortcuts import render,redirect
from datetime import datetime
from .models import Solicitud, Solicitante, Asistente_Social
from .forms import SolicitudForm, SolicitanteForm, AsistenteSocialForm
from django.db.models import Q

# Create your views here.

def base(request):
    context = {}
    return render(request, 'components/base.html',context)

def navbar(request):
    context = {}
    return render(request, 'components/navbar.html', context)


def index(request):
    context = {}
    queryset = (request.GET.get("buscarSolicitante"))
    if queryset:
        solicitante = Solicitante.objects.filter(
            Q(rutSolicitante__icontains = queryset)
        ).distinct()
        context['dataSolicitante'] = solicitante
    else:
        context = {}
    
    return render(request, 'solicitud/solicitud_index.html', context)

def addSolicitud(request):
    context = {}
    formSolicitud = SolicitudForm

    fecha = datetime.now().date()
    hora = datetime.now().time()

    context ['fechaLocal'] = fecha
    context ['horaLocal'] = hora

    if 'guardarSolicitud' in request.POST:
        formSolicitud = SolicitudForm(request.POST)
        formSolicitud.save()
        return redirect('obtener_solicitudes')

    context['formSolicitud'] = formSolicitud

    return render(request, 'solicitud/solicitud_add.html', context)

def addSolicitante(request):
    context = {}
    formSolicitante = SolicitanteForm(request.POST)

    if formSolicitante.is_valid():
        formSolicitante.save()
        return redirect('index')

    context['formSolicitante'] = formSolicitante

    return render(request, 'solicitante/solicitante_add.html', context)

def getSolicitudes(request):
    context = {}
    dataSolicitudes = Solicitud.objects.all()
    context['dataSolicitudes'] = dataSolicitudes
    return render(request, 'solicitud/solicitud_get.html', context)


def pruebas(request):
    context = {}

    asistenteSocialData = Asistente_Social.objects.all()
    solicitanteData = Solicitante.objects.all()
    solicitudData = Solicitud.objects.all()

    formAsistenteSocial = AsistenteSocialForm
    formSolicitante = SolicitanteForm
    formSolicitud = SolicitudForm

    if request.method == "POST":
        if 'guardarAsistenteSocial' in request.POST:
            formAsistenteSocial = AsistenteSocialForm(request.POST)
            formAsistenteSocial.save()

        if 'guardarSolicitante' in request.POST:
            formSolicitante = SolicitanteForm(request.POST)
            formSolicitante.save()

        if 'guardarSolicitud' in request.POST:
            formSolicitud = SolicitudForm(request.POST)
            formSolicitud.save()

    context['dataAsistenteSocial'] = asistenteSocialData
    context['dataSolcitante'] = solicitanteData
    context['dataSolicitud'] = solicitudData

    context['formAsistenteSocial'] = formAsistenteSocial
    context['formSolicitante'] = formSolicitante
    context['formSolicitud'] = formSolicitud

    return render(request, 'solicitud/pruebas.html', context)