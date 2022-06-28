from django.urls import reverse, reverse_lazy
from .models import Paciente
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Paciente

class PacienteListView(ListView):
    model = Paciente

class PacienteDetailView(DetailView):
    model = Paciente

class PacienteCreate(CreateView):
    model = Paciente
    fields = ['name','dob', 'age', 'phone', 'immediate_background']
    
    success_url = reverse_lazy('pacientes')


# Create your views here.


#def pacientes(request):
 #   pacientes = get_list_or_404(Paciente)
  #  return render(request, 'consultorio/pacientes.html', {'pacientes':pacientes})

#def paciente(request, page_id, page_slug):
 #   paciente = get_object_or_404(Paciente, id=page_id)
  #  return render(request, 'consultorio/paciente.html', {'paciente':paciente})



