from django.contrib import admin
from .models import Asistente_Social, Solicitud, Solicitante, Calle, Comuna, Detalle_Direccion, Direccion, Region

# Register your models here.

admin.site.register(Asistente_Social)
admin.site.register(Solicitud)
admin.site.register(Solicitante)
admin.site.register(Calle)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Direccion)
admin.site.register(Detalle_Direccion)