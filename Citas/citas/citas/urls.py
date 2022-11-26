"""citas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Urls App Personas
    path('personas/', include('apps.personas.urls')),      #Urls Personas
    path('empleados/', include('apps.personas.urls')),     #Url Empleados         
    path('clientes/', include('apps.personas.urls')),      #Url Clientes
    #Urls App maestra
    path('maestra/', include('apps.maestra.urls')),        #url tabla maestra
    #Urls App factura
    path('facturas/',include('apps.factura.urls')),      #Url Facturas
    path('agendas/',include('apps.factura.urls')),       #Url Agendas
]
