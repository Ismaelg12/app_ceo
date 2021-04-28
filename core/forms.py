from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError


class ListaEsperaForm(forms.ModelForm):    
    class Meta:
        model =  ListaEspera
        fields = '__all__'
        widgets = {
            'nome'                      : forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,
                'data-live-search':'true','onchange':'showDiv(this)','id':'id_nome','required': 'true',}),
			'profissional'              : forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,
                'data-live-search':'true','onchange':'showDiv(this)','id':'id_profissional','required': 'true',}),
			'especialidade'             : forms.Select(attrs={'class': 'form-control'}),
			'observacao'                : forms.Textarea(attrs={'class': 'form-control'}), 
            'urgente'                   : forms.Select(attrs={'class': 'form-control','required': 'true'}),
            'criado_em'                 : forms.DateInput(attrs={'class': 'form-control'}),
        }


    def clean(self):
        nome = self.cleaned_data['nome']
        especialidade = self.cleaned_data['especialidade']

        lista = ListaEspera.objects.filter(nome__id=nome.id, especialidade__id=especialidade.id).exists()
        if lista:
            raise ValidationError('Paciente já esta cadastrado para esta especialidade!')
