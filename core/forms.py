from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError


OP_CHOICES = (
    ('', 'Selecione . . .'),
    (True, 'Sim'),
    (False, 'Não')
)
class ListaEsperaForm(forms.ModelForm):
    profissional = forms.ModelMultipleChoiceField(
        queryset = Profissional.prof_objects.all(),
        widget   =   forms.SelectMultiple(attrs={'class':'selectpicker',
        'data-style':'select-with-transition','data-size':7,
        'data-live-search':'true','multiple':'multiple','title':'Selecione um profissional'})
    )
    
    class Meta:
        model =  ListaEspera
        fields = '__all__'
        widgets = {
            'nome'           : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
			'data_nascimento': forms.DateInput(attrs={'class': 'form-control','required': 'true'}),
			'sexo'           : forms.Select(attrs={'class': 'form-control'}),
			'cpf'            : forms.TextInput(attrs={'class': 'form-control'}),
			'sus'             : forms.TextInput(attrs={'class': 'form-control'}),
			'telefone'       : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
			'telefone_fixo'  : forms.TextInput(attrs={'class': 'form-control'}),
			'observacao'     : forms.Textarea(attrs={'class': 'form-control'}), 
            'tratamento'     : forms.Select(choices=OP_CHOICES,attrs={'class': 'form-control'}),
        }


