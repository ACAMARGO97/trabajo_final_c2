from django.contrib import admin
from apps.maestra.models import *

class TablaMaestraAdmin(admin.ModelAdmin):
    list_display = ('tama_nombre1','tama_nombre2','tama_dependencia1','tama_dependencia2','tama_codigo','tama_estado',)

admin.site.register(TablaMaestra,TablaMaestraAdmin)

