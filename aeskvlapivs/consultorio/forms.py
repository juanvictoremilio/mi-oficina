from django import forms
from .models import Paciente
from django import forms

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['name', 'gender', 'dob', 'nationality', 'etnia', 'scholarship', 'job',
     'religion', 'sport', 'civil_status', 'adress', 'email', 'phone', 'entitlement', 'specify',
     'insurance', 'immediate_background', 'smoking', 'alcohol', 'drugs_adictions', 'allergies',
     'dislipidemia', 'dm', 'hta', 'inf_ang_de_pecho', 'evc', 'ivp', 'EPOC', 'cancer', 'otras_enf',
     'cir_previas', 'obs', 'actual_situation', 'tension_sistolica', 'tension_diastolica', 'fc','fr',
     'temp', 'saturacion', 'dextrostix', 'a1c', 'peso', 'estatura', 'per_abdominal', 'Imagenología1',
     'Imagenología2', 'Imagenología3', 'Labs1', 'Labs2', 'recetas', 'diagnosis', 'obs', 'txs',

    ]
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}, ),
            
            'dob': forms.DateInput( attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa'}),
            
            'nationality': forms.TextInput(attrs={'class':'form-control'}),
            'etnia': forms.TextInput(attrs={'class':'form-control'}),
            'scholarship': forms.TextInput(attrs={'class':'form-control'}),
            'job': forms.TextInput(attrs={'class':'form-control'}),
            'adress': forms.TextInput(attrs={'class':'form-control'}),
            'immediate_background': forms.Textarea(attrs={'class':'form-control'}),
            'obs': forms.Textarea(attrs={'class':'form-control'}),
            'cir_previas': forms.TextInput(attrs={'class':'form-control'}),
            'otras_enf': forms.Textarea(attrs={'class':'form-control'}),
            'actual_situation': forms.Textarea(attrs={'class':'form-control'}),
          
            'diagnosis': forms.Textarea(attrs={'class':'form-control'}),
            'txs': forms.Textarea(attrs={'class':'form-control'}),
                        
        }
        