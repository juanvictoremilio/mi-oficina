from django.urls import path
from . import views
from consultorio.views import PacienteListView, PacienteDetailView, PacienteCreate

urlpatterns = [
    path('', PacienteListView.as_view(), name='pacientes'),
    path('<int:pk>/<slug:paciente_slug>/', PacienteDetailView.as_view(), name='paciente'),
    path('create/', views.PacienteCreate.as_view(),name='nuevo_paciente')
]




