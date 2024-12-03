from django import forms
from django.forms.widgets import DateInput, TimeInput
from .models import Solicitud, Solicitante, Detalle_Direccion, Asistente_Social, Direccion, Region, Comuna, Calle


class SolicitudForm(forms.ModelForm): 
    class Meta:
        model = Solicitud
        fields = ['nombre', 'beneficio', 'cantidadBeneficios', 'hora', 'fecha', 'fkRutAsistenteSocial', 'fkRutSolicitante']
        widgets = {
            'fecha': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'hora': TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }

class CalleForm(forms.ModelForm):
    class Meta:
        model = Calle
        fields = ['nombre', 'numero', 'avenida']

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['nombre']

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['nombre']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['fkRegion', 'fkComuna', 'fkCalle']

class AsistenteSocialForm(forms.ModelForm):
    class Meta:
        model = Asistente_Social
        fields = ['rutAsistenteSocial', 'nombres', 'apellidos', 'telefono', 'edad', 'correo', 'fkDireccion']

class DetalleDireccionForm(forms.ModelForm):
    class Meta:
        model = Detalle_Direccion
        fields = ['casa', 'poblacion_villa_condominio', 'unidadVecinal', 'depto', 'block_edificio']

class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ['rutSolicitante', 'primerNombre', 'segundoNombre', 'primerApellido', 'segundoApellido', 'telefono', 'edad', 'correo', 'grupoFamiliar', 'fkDireccion', 'fkDetalleDireccion']