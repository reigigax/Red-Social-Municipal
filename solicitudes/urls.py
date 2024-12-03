from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solicitudes', views.getSolicitudes, name='obtener_solicitudes'),
    
    path('pruebas', views.pruebas, name='pruebas'),
]