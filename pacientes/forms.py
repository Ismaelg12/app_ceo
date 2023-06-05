from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError


class PacienteForm(forms.ModelForm):
	class Meta:
		model   = Paciente
		fields  = '__all__'
		widgets = {
			'nome'           : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
			'data_nascimento': forms.DateInput(attrs={'class': 'form-control','required': 'true'}),
			'sexo'           : forms.Select(attrs={'class': 'form-control'}),
			'cpf'            : forms.TextInput(attrs={'class': 'form-control'}),
			'sus'            : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
			'cidade'         : forms.TextInput(attrs={'class': 'form-control'}),
			'rua'            : forms.TextInput(attrs={'class': 'form-control'}),
			'numero'         : forms.TextInput(attrs={'class': 'form-control'}),
			'bairro'         : forms.TextInput(attrs={'class': 'form-control'}),
			'telefone'       : forms.TextInput(attrs={'class': 'form-control','required': 'true', 'onkeyup':'mascaraFone(event)'}),
			'observacao'     : forms.Textarea(attrs={'class': 'form-control'}),
			'ubs'            : forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,
                'data-live-search':'true','onchange':'showDiv(this)','id':'id_ubs','required': 'true',}),
		}

