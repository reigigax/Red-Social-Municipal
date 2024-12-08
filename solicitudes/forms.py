from django import forms
from django.utils.timezone import now, localtime
from .models import Solicitud, Solicitante, Asistente_Social
from django.core.exceptions import ValidationError
import re

class SolicitudForm(forms.ModelForm): 
    class Meta:
        model = Solicitud
        fields = ['nombreCasoSolicitud', 'beneficio', 'cantidadBeneficios', 'hora', 'fecha', 'fkRutAsistenteSocial', 'fkRutSolicitante', 'descripcionBeneficio','nombreCalle','numeroCalle', 'nombreAvenida','nombreComuna','nombreRegion','casa', 'poblacion_villa_condominio', 'unidadVecinal', 'depto', 'block_edificio']
        labels = {
            'nombreCasoSolicitud':'Nombre del Caso',
            'beneficio':'Tipo de Beneficio',
            'cantidadBeneficios':'N° Beneficios',
            'fkRutAsistenteSocial':'Asistente Social',
            'fkRutSolicitante':'Solicitante',
            'descripcionBeneficio':'Descripción del Beneficio',

            'nombreCalle': 'Calle',
            'numeroCalle': 'Numero',
            'nombreAvenida': 'Avenida',

            'nombreComuna': 'Comuna',
            'nombreRegion': 'Region',

            'casa': 'Casa',
            'poblacion_villa_condominio': 'Población/Villa/Condominio',
            'unidadVecinal': 'Unidad Vecinal',
            'depto': 'Departamento',
            'block_edificio': 'Block/Edificio'
        }
        widgets = {
            'nombreCasoSolicitud': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el Nombre del Caso'}),
            'beneficio': forms.TextInput(attrs={'class': 'form-control','placeholder':'Tipo/s de Beneficio/s'}),
            'cantidadBeneficios': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'N° Beneficios'}),
            'descripcionBeneficio': forms.Textarea(attrs={'rows': 4 ,'class': 'form-control', 'placeholder': 'Descripción del Beneficio y Detalles del Solicitante'}),

            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(format='%H:%M', attrs={'type': 'time','class': 'form-control'}),
            
            'nombreCalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la Calle'}),
            'numeroCalle': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'N° de la Calle'}),
            'nombreAvenida': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la Avenida'}),

            'nombreComuna': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la Comuna'}),
            'nombreRegion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la Region'}),

            'casa': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingresar Casa'}),
            'poblacion_villa_condominio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Población/Villa/Condominio'}),
            'unidadVecinal': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'N° Unidad Vecinal'}),
            'depto': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingresar Departamento'}),
            'block_edificio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Block/Edificio'}),

            'fkRutAsistenteSocial': forms.Select(attrs={'class': 'form-select'}),
            'fkRutSolicitante': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].initial = localtime(now()).date()
        self.fields['hora'].initial = localtime(now()).time()
        self.fields['fkRutAsistenteSocial'].empty_label = None
        self.fields['fkRutSolicitante'].empty_label = None
        self.fields['fkRutAsistenteSocial'].choices = [('', 'Selecciona un Asistene Social')] + list(self.fields['fkRutAsistenteSocial'].choices)
        self.fields['fkRutSolicitante'].choices = [('', 'Selecciona un Solicitante')] + list(self.fields['fkRutSolicitante'].choices)

    def clean(self):
        cleaned_data = super().clean()
        
        if not cleaned_data.get('fecha'):
            cleaned_data['fecha'] = localtime(now()).date()
        
        if not cleaned_data.get('hora'):
            cleaned_data['hora'] = localtime(now()).time()
        
        return cleaned_data


class AsistenteSocialForm(forms.ModelForm):
    class Meta:
        model = Asistente_Social
        fields = ['rutAsistenteSocial', 'nombres', 'apellidos', 'telefono', 'edad', 'correo']


class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ['rutSolicitante', 'primerNombre', 'segundoNombre', 'primerApellido', 'segundoApellido', 'telefono', 'edad', 'correo', 'grupoFamiliar']
        labels = {
            'rutSolicitante': 'RUN Solicitante',
            'primerNombre': 'Primer Nombre',
            'segundoNombre': 'Segundo Nombre',
            'primerApellido': 'Primer Apellido',
            'segundoApellido': 'Segundo Apellido',
            'telefono': 'Telefono',
            'edad': 'Edad',
            'correo': 'Correo',
            'grupoFamiliar': 'Grupo Familiar',
        }
        widgets = {
            'rutSolicitante': forms.TextInput(attrs={'class':'form-control', 'placeholder':'RUN de Solicitante'}),
            'primerNombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Primer Nombre'}),
            'segundoNombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo Nombre o Nombres'}),
            'primerApellido': forms.TextInput(attrs={'class':'form-control','placeholder':'Primer Apellido'}),
            'segundoApellido': forms.TextInput(attrs={'class':'form-control','placeholder':'Segundo Apellido o Apellidos'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control','placeholder':'Numero de Telefono'}),
            'edad': forms.NumberInput(attrs={'class':'form-control','placeholder':'Edad'}),
            'correo': forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo del Solicitante'}),
            'grupoFamiliar': forms.TextInput(attrs={'class':'form-control','placeholder':'Grupo Familiar'}),
        }