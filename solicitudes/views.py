from django.shortcuts import render
from .models import Solicitud, Solicitante, Detalle_Direccion, Asistente_Social, Direccion, Region, Calle, Comuna
from .forms import SolicitudForm, SolicitanteForm, DetalleDireccionForm, AsistenteSocialForm, DireccionForm, RegionForm, ComunaForm, CalleForm

# Create your views here.

def index(request):
    context = {}
    form = SolicitudForm
    context['form'] = form
    return render(request, 'solicitud/solicitud_index.html', context)

def getSolicitudes(request):
    context = {}
    return render(request, 'solicitud/solicitud_get.html', context)


def pruebas(request):
    context = {}

    calleData = Calle.objects.all()
    comunaData = Comuna.objects.all()
    regionData = Region.objects.all()
    direccionData = Direccion.objects.all()
    asistenteSocialData = Asistente_Social.objects.all()
    detalleDireccionData = Detalle_Direccion.objects.all()
    solicitanteData = Solicitante.objects.all()
    solicitudData = Solicitud.objects.all()

    formCalle = CalleForm
    formComuna = ComunaForm
    formRegion = RegionForm
    formDireccion = DireccionForm
    formAsistenteSocial = AsistenteSocialForm
    formDetalleDireccion = DetalleDireccionForm
    formSolicitante = SolicitanteForm
    formSolicitud = SolicitudForm

    if request.method == "POST":
        if 'guardarCalle' in request.POST:
            formCalle = CalleForm(request.POST)
            formCalle.save()

        if 'guardarComuna' in request.POST:
            formComuna = ComunaForm(request.POST)
            formComuna.save()

        if 'guardarRegion' in request.POST:
            formRegion = RegionForm(request.POST)
            formRegion.save()

        if 'guardarDireccion' in request.POST:
            formDireccion = DireccionForm(request.POST)
            formDireccion.save()

        if 'guardarAsistenteSocial' in request.POST:
            formAsistenteSocial = AsistenteSocialForm(request.POST)
            formAsistenteSocial.save()

        if 'guardarDetalleDireccion' in request.POST:
            formDetalleDireccion = DetalleDireccionForm(request.POST)
            formDetalleDireccion.save()

        if 'guardarSolicitante' in request.POST:
            formSolicitante = SolicitanteForm(request.POST)
            formSolicitante.save()

        if 'guardarSolicitud' in request.POST:
            formSolicitud = SolicitudForm(request.POST)
            formSolicitud.save()


    context['dataCalle'] = calleData
    context['dataComuna'] = comunaData
    context['dataRegion'] = regionData
    context['dataDireccion'] = direccionData
    context['dataAsistenteSocial'] = asistenteSocialData
    context['dataDetalleDireccion'] = detalleDireccionData
    context['dataSolcitante'] = solicitanteData
    context['dataSolicitud'] = solicitudData

    context['formCalle'] = formCalle
    context['formComuna'] = formComuna
    context['formRegion'] = formRegion
    context['formDireccion'] = formDireccion
    context['formAsistenteSocial'] = formAsistenteSocial
    context['formDetalleDireccion'] = formDetalleDireccion
    context['formSolicitante'] = formSolicitante
    context['formSolicitud'] = formSolicitud

    return render(request, 'solicitud/pruebas.html', context)