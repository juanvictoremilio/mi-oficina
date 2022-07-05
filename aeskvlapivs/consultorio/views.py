from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .models import Paciente
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Paciente
from .forms import PacienteForm
from core.views import HomePageView

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    

class PacienteDetailView(DetailView):
    model = Paciente
    
@method_decorator(staff_member_required, name='dispatch')
class PacienteCreate(CreateView):
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy('consultorio:pacientes')

@method_decorator(staff_member_required, name='dispatch')
class PacienteUpdate(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('consultorio:Actualizar Paciente', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PacienteDeleteView(DeleteView):
    model = Paciente
    success_url = reverse_lazy('consultorio:pacientes')




# Create your views here.


#def pacientes(request):
 #   pacientes = get_list_or_404(Paciente)
  #  return render(request, 'consultorio/pacientes.html', {'pacientes':pacientes})

#def paciente(request, page_id, page_slug):
 #   paciente = get_object_or_404(Paciente, id=page_id)
  #  return render(request, 'consultorio/paciente.html', {'paciente':paciente})



