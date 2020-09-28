from django import forms
from agenda.models import Agendamento
from controle_usuarios.models import Profissional
from pacientes.models import Paciente


OP_CHOICES = (
    ('', 'Escolha Um Opçao'),
    (True, 'Sim'),
    (False, 'Não')
)

class AgendaForm(forms.ModelForm):

    class Meta:
        model   = Agendamento
        fields  = '__all__'
        widgets = {
            'data'        : forms.DateInput(attrs={'class': 'form-control','required': 'true'}),
            'hora' 		  : forms.TimeInput(attrs={'class': 'form-control input-rounded'}),
            'paciente'    : forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition',
                'data-size':7,'data-live-search':'true','required': 'true'}),
            'profissional': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition',
                'data-size':7,'data-live-search':'true','required': 'true'}),
            'telefone'    : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
            'status'      : forms.Select(attrs={'class': 'selectpicker','data-style':'select-with-transition', 'required':'True'}),
            'observacao'  : forms.Textarea(attrs={'class': 'form-control','cols' : "10", 'rows': "3",}),
        }
    
