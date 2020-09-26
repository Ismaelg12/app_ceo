from django import forms
from .models import Produto, Categoria


class ProdutoForm(forms.ModelForm):

    class Meta:
        model =  Produto
        fields = '__all__'
        widgets = {
        	'produto'    	: forms.TextInput(attrs={'class': 'form-control','required': 'true' }),
        	'estoque'       : forms.TextInput(attrs={'class': 'form-control'}),
        	'estoque_minimo': forms.TextInput(attrs={'class': 'form-control'}),
        	'validade'   	: forms.DateInput(attrs={'class': 'form-control','required': 'true'}),
        	'categoria'     : forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,
                'data-live-search':'true','required': 'true','onchange':'showDiv(this)','id':'id_categoria',}),
}
class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'