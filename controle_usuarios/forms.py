from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from controle_usuarios.models import Profissional

TRUE_FALSE_CHOICES = (
    (True, 'Sim'),
    (False, 'Não')
)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control',})    
  

class ProfissinalForm(forms.ModelForm):
    class Meta:
        model   = Profissional
        exclude = ['user']
        fields  = '__all__'
        widgets = {
            'user'            : forms.Select(attrs={'class': 'form-control '}),
            'nome'            : forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome'       : forms.TextInput(attrs={'class': 'form-control'}),
            'email'           : forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone'        : forms.TextInput(attrs={'class': 'form-control'}),
            'registro'        : forms.TextInput(attrs={'class': 'form-control'}),
            'cpf'             : forms.TextInput(attrs={'class': 'form-control',}),
            'especialidade'   : forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition',
                'data-size':7,'data-live-search':'true','required': 'true','id':'id_especialidade',}),
            'data_nascimento' : forms.DateInput(attrs={'class': 'form-control',}),
            'tipo'            : forms.Select(attrs={'class': 'selectpicker',
            'data-style':'select-with-transition','data-size':7,'required': 'true',}),
            'ativo'           : forms.Select(choices=TRUE_FALSE_CHOICES,attrs={
                'class': 'selectpicker','required': 'true',
                'data-style':'select-with-transition','data-size':7}),
            'atent_categoria' : forms.TextInput(attrs={'class': 'form-control'}), 
            'observacao'      : forms.TextInput(attrs={'class': 'form-control'}), 
            
		}