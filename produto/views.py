import csv
import io
import pandas as pd
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from produto.actions.export_xlsx import export_xlsx
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm


def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(produto__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)


class ProdutoList(ListView):
    model = Produto
    template_name = 'produto_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ProdutoList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(produto__icontains=search) |
                Q(ncm__icontains=search)
            )
        return queryset


def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def produto_add(request):
    form = ProdutoForm(request.POST or None)
    template_name = 'produto_form2.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto_list'))

    context = {'form': form}
    return render(request, template_name, context)


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


def produto_json(request, pk):
    ''' Retorna o produto, id e estoque. '''
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})


def save_data(data):
    '''
    Salva os dados no banco.
    '''
    aux = []
    for item in data:
        produto = item.get('produto')
        validade = item.get('validade')
        estoque = item.get('estoque')
        estoque_minimo = item.get('estoque_minimo')
        obj = Produto(
            produto=produto,
            validade=validade,
            estoque=estoque,
            estoque_minimo=estoque_minimo,
        )
        aux.append(obj)
    Produto.objects.bulk_create(aux)

def exportar_produtos_xlsx(request):
    MDATA = datetime.now().strftime('%Y-%m-%d')
    model = 'Produto'
    filename = 'produtos_exportados.xlsx'
    _filename = filename.split('.')
    filename_final = f'{_filename[0]}_{MDATA}.{_filename[1]}'
    queryset = Produto.objects.all().values_list(
        'produto',
        'validade',
        'estoque',
        'estoque_minimo',
        'categoria__categoria',
    )
    columns = ('Produto', 'Validade',
               'Estoque', 'Estoque mínimo', 'Categoria')
    response = export_xlsx(model, filename_final, queryset, columns)
    return response

## Cadastro de Categoria

class CategoriaCreateView(CreateView):
    model         = Categoria
    template_name = 'categorias/categoria_add.html'
    form_class    = CategoriaForm
    success_url   = reverse_lazy('categorias')
    #salvar e adicionar novo
    def post(self, request, *args, **kwargs):
        save_action = None
        if "cancelar" in request.POST:
            return HttpResponseRedirect(reverse('categorias'))
        else:
            save_action = super(CategoriaCreateView, self).post(request, *args, **kwargs)
        if "adicionar_outro" in request.POST:
            messages.success(request,'Categoria Cadastrado com Sucesso! ')
            return HttpResponseRedirect(reverse('add_categoria'))
        return save_action

class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'categorias/categoria_list.html'

class CategoriaUpdateView(UpdateView):
    model         = Categoria
    template_name = 'categorias/categoria_add.html'
    form_class    = CategoriaForm
    success_url   = reverse_lazy('categorias')