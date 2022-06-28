from django.urls import path
from . import views
from consultorio.views import PacienteListView, PacienteDetailView

urlpatterns = [
    path('', PacienteListView.as_view(), name='pacientes'),
    path('<int:pk>/<slug:page_slug>/', PacienteDetailView.as_view(), name='paciente'),
]




