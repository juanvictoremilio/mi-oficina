from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Paciente
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Paciente

class PacienteListView(ListView):
    model = Paciente

class PacienteDetailView(DetailView):
    model = Paciente


# Create your views here.


#def pacientes(request):
 #   pacientes = get_list_or_404(Paciente)
  #  return render(request, 'consultorio/pacientes.html', {'pacientes':pacientes})

#def paciente(request, page_id, page_slug):
 #   paciente = get_object_or_404(Paciente, id=page_id)
  #  return render(request, 'consultorio/paciente.html', {'paciente':paciente})



