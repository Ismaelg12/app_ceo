from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError


class PacienteForm(forms.ModelForm):
	profissional = forms.ModelMultipleChoiceField(
		queryset = Profissional.objects.filter(tipo=2),
		widget   =   forms.SelectMultiple(attrs={'class':'selectpicker',
		'data-style':'select-with-transition','data-size':7,
		'data-live-search':'true','multiple':'multiple','title':'escolha os profissionais'})
	)

	class Meta:
		model   = Paciente
		fields  = '__all__'
		widgets = {
			'nome'           : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
			'data_nascimento': forms.DateInput(attrs={'class': 'form-control','required': 'true'}),
			'sexo'           : forms.Select(attrs={'class': 'form-control'}),
			'cpf'            : forms.TextInput(attrs={'class': 'form-control'}),
			'sus'            : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
			'telefone'       : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
			'telefone_fixo'  : forms.TextInput(attrs={'class': 'form-control'}),
			'observacao'     : forms.Textarea(attrs={'class': 'form-control'}),
			'tratamento'     : forms.Select(attrs={'class': 'form-control'}),
		}

