from django.contrib import admin
from apps.personas.models import *
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('pers_nombre','pers_apellido','pers_telefono','tiposexo')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('persona','clie_nacionalidad','tipocliente')

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('empl_nacionalidad','persona','tipoempleado')


admin.site.register(Personas,PersonaAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Cliente,ClienteAdmin)
