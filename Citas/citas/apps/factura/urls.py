from django.urls import path
from .views import *
from ..consultas import *

urlpatterns = [
    #Url Factura
    path('f', FacturaView.as_view()),
    path('fcreate/', FacturaCreate.as_view()),
    path('fupdate/<int:pk>/', FacturaUpdate.as_view()),
    path('fdelete/<int:pk>/', FacturaDelete.as_view()),
    path('fall/', FacturaViewOwner.as_view()),
    path('consulta1/', Consulta1.as_view()),
    path('consulta2/', Consulta2.as_view()),
    path('consulta3/', Consulta3.as_view()),

    #Url Agenda
    path('a', AgendaView.as_view()),
    path('acreate/', AgendaCreate.as_view()),
    path('aupdate/<int:pk>/', AgendaUpdate.as_view()),
    path('adelete/<int:pk>/', AgendaDelete.as_view()),
    path('aall/', AgendaViewOwner.as_view()),
]