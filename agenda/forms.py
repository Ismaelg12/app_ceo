from django import forms
from agenda.models import Agendamento, Odontograma, Procedimento, Vigilancia
from controle_usuarios.models import Profissional, Especialidade
from pacientes.models import Paciente, Ubs
from django.core.exceptions import ValidationError


OP_CHOICES = (
    ('', 'Escolha Um Opçao'),
    (True, 'Sim'),
    (False, 'Não')
)


    

class AgendaForm(forms.ModelForm):
    #filtra apenas os profissionais que trabalham como fisioterapeutas
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profissional'].queryset = Profissional.objects.filter(tipo=2,ativo=True)
        # self.fields['paciente'].label_from_instance = self.paciente_label
        self.fields['profissional'].label_from_instance = self.profissional_label
        self.fields['especialidade'].queryset = Especialidade.objects.all().exclude(id="1")
    #campo select ajax    
        self.fields['paciente'].queryset = Paciente.objects.none()
        if 'paciente' in self.data:
            self.fields['paciente'].queryset = Paciente.objects.all()
        elif self.instance.pk:
            self.fields['paciente'].queryset = Paciente.objects.all().filter(pk=self.instance.paciente.pk)
    #metodo para override de labels do pacientes
    # @staticmethod
    # def paciente_label(self):
    #     return str(self.nome) + ' -- ' + self.telefone + ' -- ' + str(self.ubs)

    @staticmethod
    def profissional_label(self):
        return str(self.nome) + '--' + str(self.especialidade)

    odontograma = forms.ModelMultipleChoiceField(
        queryset = Odontograma.objects.all(),
        widget   =   forms.SelectMultiple(attrs={'class':'selectpicker',
        'data-style':'select-with-transition','data-size':7,
        'data-live-search':'true','multiple':'multiple','title':'Selecine'})
    )

    vigilancia = forms.ModelMultipleChoiceField(
        queryset = Vigilancia.objects.all(),
        widget   =   forms.CheckboxSelectMultiple(attrs={'class':'selectpicker',
        'data-style':'select-with-transition','multiple':'multiple','title':'Selecione'})
    )

    procedimento = forms.ModelMultipleChoiceField(
        queryset = Procedimento.objects.all(),
        widget   =   forms.SelectMultiple(attrs={'class':'selectpicker',
        'data-style':'select-with-transition','data-size':7,
        'data-live-search':'true','multiple':'multiple','title':'Selecione'})
    )

    class Meta:
        model   = Agendamento
        fields  = '__all__'
        widgets = {
            'data'        : forms.DateInput(attrs={'class': 'form-control','required': 'true'}),
            'hora' 		  : forms.TimeInput(attrs={'class': 'form-control input-rounded'}),
            'paciente'    : forms.Select(attrs={'class':'form-select','required': 'true'}),
            'telefone'    : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
            'especialidade'    : forms.Select(attrs={'class':'form-select','required': 'true'}),
            'profissional': forms.Select(attrs={'class':'form-select','required': 'true'}),
            'status'      : forms.Select(attrs={'class': 'form-select','data-style':'select-with-transition', 'required':'True'}),
            'observacao'  : forms.Textarea(attrs={'class': 'form-control','cols' : "20", 'rows': "5",}),
            'ubs'            : forms.Select(attrs={'class':'form-select','required': 'true',}),
            'tipoconsulta'            : forms.RadioSelect(attrs={'class':'selectpicker','required': 'true','title':'Selecione',}),
        }


        
    