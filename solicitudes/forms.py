from django import forms
from django.utils.timezone import now, localtime
from .models import Solicitud, Solicitante, Detalle_Direccion, Asistente_Social, Direccion, Region, Comuna, Calle


class SolicitudForm(forms.ModelForm): 
    class Meta:
        model = Solicitud
        fields = ['nombre', 'beneficio', 'cantidadBeneficios', 'hora', 'fecha', 'fkRutAsistenteSocial', 'fkRutSolicitante']
        labels = {
            'nombre':'Nombre del Caso',
            'beneficio':'Tipo de Beneficio',
            'cantidadBeneficios':'N° Beneficios',
            'fkRutAsistenteSocial':'Asistente Social',
            'fkRutSolicitante':'Solicitante'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el Nombre del Caso'}),
            'beneficio': forms.TextInput(attrs={'class': 'form-control','placeholder':'Tipo/s de Beneficio/s'}),
            'cantidadBeneficios': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'N° Beneficios'}),

            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(format='%H:%M', attrs={'type': 'time','class': 'form-control'}),

            'fkRutAsistenteSocial': forms.Select(attrs={'class': 'form-select'}),
            'fkRutSolicitante': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].initial = localtime(now()).date()
        self.fields['hora'].initial = localtime(now()).time()
        self.fields['fkRutAsistenteSocial'].choices = [('', 'Selecciona un Asistene Social')] + list(self.fields['fkRutAsistenteSocial'].choices)
        self.fields['fkRutSolicitante'].choices = [('', 'Selecciona un Solicitante')] + list(self.fields['fkRutSolicitante'].choices)

    def clean(self):
        cleaned_data = super().clean()
        
        if not cleaned_data.get('fecha'):
            cleaned_data['fecha'] = localtime(now()).date()
        
        if not cleaned_data.get('hora'):
            cleaned_data['hora'] = localtime(now()).time()
        
        return cleaned_data


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