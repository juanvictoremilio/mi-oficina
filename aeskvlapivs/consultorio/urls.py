from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import PacienteListView, PacienteDetailView, PacienteCreate, PacienteUpdate, PacienteDeleteView, SearchResultsView

app_name = "consultorio"


consultorio_patterns = ([
    path('', PacienteListView.as_view(), name='pacientes'),
    path("upload", views.uploadFile, name = "uploadFile"),
    path('<int:pk>/<slug:paciente_slug>/', PacienteDetailView.as_view(), name='paciente'),
    path('<int:pk>/<slug:paciente_slug>/', PacienteDetailView.as_view(), name='historia'),
    path('create/', PacienteCreate.as_view(),name='nuevo_paciente'),
    path('update/<int:pk>/', PacienteUpdate.as_view(),name='Actualizar Paciente'),
    path('delete/<int:pk>/', PacienteDeleteView.as_view(),name='eliminar paciente'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
   

   
], 'consultorio')




