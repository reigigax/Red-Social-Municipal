from django.db import models

#  Create your models here.

class Asistente_Social(models.Model):
    rutAsistenteSocial = models.CharField(max_length=13, primary_key=True)
    nombres = models.CharField(max_length=150, blank=False, null=False)
    apellidos = models.CharField(max_length=150, blank=False, null=False)
    telefono = models.IntegerField(blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    correo = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return str(self.nombres +" "+ self.apellidos)


class Solicitante(models.Model):
    rutSolicitante = models.CharField(max_length=13, primary_key=True)
    primerNombre = models.CharField(max_length=100, blank=False, null=False)
    segundoNombre = models.CharField(max_length=160, blank=True, null=True)
    primerApellido = models.CharField(max_length=100, blank=False, null=False)
    segundoApellido = models.CharField(max_length=160, blank=True, null=True)
    telefono = models.IntegerField(blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    correo = models.EmailField(max_length=150, blank=False, null=False)
    grupoFamiliar = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return str(self.rutSolicitante)


class Solicitud(models.Model):
    numeroSolicitud = models.AutoField(db_column='n_solicitud', primary_key=True)
    nombreCasoSolicitud = models.CharField(max_length=150, blank=False, null=False)
    beneficio = models.CharField(max_length=250, blank=False, null=False)
    descripcionBeneficio = models.CharField(max_length=2500, blank=True, null=True)
    cantidadBeneficios = models.IntegerField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)

    nombreCalle = models.CharField(max_length=90, blank=False, null=False)
    numeroCalle = models.IntegerField(blank=False, null=False)
    nombreAvenida = models.CharField(max_length=90, blank=False, null=False)

    nombreComuna = models.CharField(max_length=90, blank=False, null=False)
    nombreRegion = models.CharField(max_length=90, blank=False, null=False)

    casa = models.CharField(max_length=90, blank=False, null=False)
    poblacion_villa_condominio = models.CharField(max_length=90, blank=False, null=False)
    unidadVecinal = models.CharField(max_length=90, blank=False, null=False)
    depto = models.CharField(max_length=90, blank=True, default='Sin Especificar')
    block_edificio = models.CharField(max_length=90, blank=True, default='Sin Especificar')

    fkRutAsistenteSocial = models.ForeignKey('Asistente_Social', on_delete=models.CASCADE, db_column='rutAsistenteSocial')
    fkRutSolicitante = models.ForeignKey('Solicitante', on_delete=models.CASCADE, db_column='rutSolicitante')
