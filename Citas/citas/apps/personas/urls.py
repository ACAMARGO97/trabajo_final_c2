from django.urls import path
from .views import *

urlpatterns = [
    #Url Personas
    path('', PersonasView.as_view()),
    path('create/', PersonasCreate.as_view()),
    path('update/<int:pk>/', PersonasUpdate.as_view()),
    path('delete/<int:pk>/', PersonasDelete.as_view()),
    path('all/', PersonasViewOwner.as_view()),

    #Urls Clientes
    path('c', ClienteView.as_view()),
    path('ccreate/', ClienteCreate.as_view()),
    path('cupdate/<int:pk>/', ClienteUpdate.as_view()),
    path('cdelete/<int:pk>/', ClienteDelete.as_view()),
    path('call/', ClienteViewOwner.as_view()),

    #Urls Propietario
    path('e', EmpleadoView.as_view()),
    path('ecreate/', EmpleadoCreate.as_view()),
    path('eupdate/<int:pk>/', EmpleadoUpdate.as_view()),
    path('edelete/<int:pk>/', EmpleadoDelete.as_view()),
    path('eall/', EmpleadoViewOwner.as_view()),
]