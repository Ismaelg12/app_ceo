from django import forms
from django.forms import ModelForm
from .models import *



class ListaEsperaForm(forms.ModelForm):  
    #filtra apenas os profissionais que atendem
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].label_from_instance = self.paciente_label
    #metodo para override de labels do pacientes
    @staticmethod
    def paciente_label(self):
        return str(self.nome) + '--' + self.telefone
    class Meta:
        model =  ListaEspera
        fields = '__all__'
        widgets = {
            'nome'    : forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition',
                'data-size':7,'data-live-search':'true','required': 'true','id':'id_nome',}),
			'telefone'    : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
			'especialidade'             : forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition',
                'data-size':7,'data-live-search':'true','required': 'true','id':'id_especialidade',}),
			'observacao'                : forms.Textarea(attrs={'class': 'form-control'}), 
            'urgente'                   : forms.Select(attrs={'class': 'form-control','required': 'true'}),
            'ligacao'                   : forms.Select(attrs={'class': 'form-control','required': 'true'}),
            'criado_em'                 : forms.DateInput(attrs={'class': 'form-control','required': 'true'}),
        }


    # def clean(self):
    #     nome = self.cleaned_data['nome']
    #     especialidade = self.cleaned_data['especialidade']

    #     lista = ListaEspera.objects.filter(nome__id=nome.id, especialidade__id=especialidade.id).exists()
    #     if lista:
    #         raise ValidationError('Paciente já esta cadastrado para esta especialidade!')
