from django import forms
from agenda.models import Agendamento
from controle_usuarios.models import Profissional
from pacientes.models import Paciente
from django.core.exceptions import ValidationError


OP_CHOICES = (
    ('', 'Escolha Um Opçao'),
    (True, 'Sim'),
    (False, 'Não')
)

class AgendaForm(forms.ModelForm):
    #filtra apenas os profissionais que atendem
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profissional'].queryset = Profissional.objects.filter(tipo=2,ativo=True)
        self.fields['paciente'].label_from_instance = self.paciente_label
    #metodo para override de labels do pacientes
    @staticmethod
    def paciente_label(self):
        return str(self.nome[:30]) + ' -- ' + self.telefone

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
    
    # def clean(self):
    #     paciente = self.cleaned_data['paciente']
    #     hora = self.cleaned_data['hora']
    #     profissional = self.cleaned_data['profissional']

    #     lista = Agendamento.objects.filter(paciente__id=paciente.id, hora=hora, profissional__id=profissional.id).exists()
    #     if lista:
    #         raise ValidationError('Paciente já tem um agendameno!')