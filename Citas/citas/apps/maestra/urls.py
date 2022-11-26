from django.urls import path
from .views import *

urlpatterns = [
        #Url TablaMaestra
    path('m', TablaMaestraView.as_view()),
    path('mcreate/', TablaMaestraCreate.as_view()),
    path('mupdate/<int:pk>/', TablaMaestraUpdate.as_view()),
    path('mdelete/<int:pk>/', TablaMaestraDelete.as_view()),
    path('mall/', TablaMaestraViewOwner.as_view()),

]