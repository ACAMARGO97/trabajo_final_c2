from django.contrib import admin
from apps.factura.models import *

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('fact_nombre','fact_precio','tiposervicio')

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('agen_numero','agen_fecha','cliente','empleado','factura')

admin.site.register(Factura,FacturaAdmin)
admin.site.register(Agenda,AgendaAdmin)



