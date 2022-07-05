from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['name', 'gender', 'dob', 'nationality', 'etnia', 'scholarship', 'job',
     'religion', 'sport', 'civil_status', 'adress', 'email', 'phone', 'entitlement', 'specify',
     'insurance', 'immediate_background']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}, ),
            
            'dob': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa'}),
            
            'nationality': forms.TextInput(attrs={'class':'form-control'}),
            'etnia': forms.TextInput(attrs={'class':'form-control'}),
            'scholarship': forms.TextInput(attrs={'class':'form-control'}),
            'job': forms.TextInput(attrs={'class':'form-control'}),
            'adress': forms.TextInput(attrs={'class':'form-control'}),
            'immediate_background': forms.Textarea(attrs={'class':'form-control'}),
                        
        }