from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solicitudes', views.getSolicitudes, name='obtener_solicitudes'),
    path('ingresar_solicitud', views.addSolicitud, name='ingresar_solicitud'),
    path('ingresar_solicitente', views.addSolicitante, name='ingresar_solicitante'),

    
    path('base', views.base, name='pruebas_base'),
    path('navbar', views.navbar, name='pruebas_navbar'),

    path('pruebas', views.pruebas, name='pruebas'),
]