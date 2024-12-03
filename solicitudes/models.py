from django.db import models

# Create your models here.

class Calle(models.Model):
    idCalle = models.AutoField(db_column='id_calle', primary_key=True)
    nombre = models.CharField(max_length=90, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    avenida = models.CharField(max_length=90, blank=False, null=False)

    def __str__(self):
        formato_numero = str(self.numero)
        return str(self.nombre +" "+ formato_numero +", "+ self.avenida)


class Comuna(models.Model):
    idComuna = models.AutoField(db_column='id_comuna', primary_key=True)
    nombre = models.CharField(max_length=90, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)


class Region(models.Model):
    idRegion = models.AutoField(db_column='id_region', primary_key=True)
    nombre = models.CharField(max_length=90, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)


class Direccion(models.Model):
    idDireccion = models.AutoField(db_column='id_direccion', primary_key=True)
    fkComuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, db_column='id_comuna')
    fkRegion = models.ForeignKey('Region', on_delete=models.CASCADE, db_column='id_region')
    fkCalle = models.ForeignKey('Calle', on_delete=models.CASCADE, db_column='id_calle')

    def __str__(self):
        return f"{self.fkCalle}, {self.fkComuna} ({self.fkRegion})"


class Asistente_Social(models.Model):
    rutAsistenteSocial = models.CharField(max_length=13, primary_key=True)
    nombres = models.CharField(max_length=150, blank=False, null=False)
    apellidos = models.CharField(max_length=150, blank=False, null=False)
    telefono = models.IntegerField(blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    correo = models.CharField(max_length=150, blank=False, null=False)
    fkDireccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, db_column='id_direccion')

    def __str__(self):
        return str(self.nombres +" "+ self.apellidos)


class Detalle_Direccion(models.Model):
    idDetalleDireccion = models.AutoField(db_column='id_detalle_direccion', primary_key=True)
    casa = models.CharField(max_length=90, blank=False, null=False)
    poblacion_villa_condominio = models.CharField(max_length=90, blank=False, null=False)
    unidadVecinal = models.CharField(max_length=90, blank=False, null=False)
    depto = models.CharField(max_length=90, blank=False)
    block_edificio = models.CharField(max_length=90, blank=False)

    def __str__(self):
        return str(self.casa +" "+ self.poblacion_villa_condominio +" "+ self.unidadVecinal +" "+ self.depto +" "+ self.block_edificio)


class Solicitante(models.Model):
    rutSolicitante = models.CharField(max_length=13, primary_key=True)
    primerNombre = models.CharField(max_length=100, blank=False, null=False)
    segundoNombre = models.CharField(max_length=160, blank=False, null=False)
    primerApellido = models.CharField(max_length=100, blank=False, null=False)
    segundoApellido = models.CharField(max_length=160, blank=False, null=False)
    telefono = models.IntegerField(blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False)
    correo = models.CharField(max_length=150, blank=False, null=False)
    grupoFamiliar = models.CharField(max_length=150, blank=False, null=False)
    fkDireccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, db_column='id_direccion')
    fkDetalleDireccion = models.ForeignKey('Detalle_Direccion', on_delete=models.CASCADE, db_column='id_detalle_direccion')

    def __str__(self):
        return str(self.rutSolicitante)


class Solicitud(models.Model):
    numeroSolicitud = models.AutoField(db_column='n_solicitud', primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    beneficio = models.CharField(max_length=250, blank=False, null=False)
    cantidadBeneficios = models.IntegerField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)

    fkRutAsistenteSocial = models.ForeignKey('Asistente_Social', on_delete=models.CASCADE, db_column='rutAsistenteSocial')
    fkRutSolicitante = models.ForeignKey('Solicitante', on_delete=models.CASCADE, db_column='rutSolicitante')
