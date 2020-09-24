from django.urls import path
from produto import views as v


urlpatterns = [
    path('', v.ProdutoList.as_view(), name='produto_list'),
    path('<int:pk>/', v.produto_detail, name='produto_detail'),
    path('add/', v.ProdutoCreate.as_view(), name='produto_add'),
    path('add2/', v.produto_add, name='produto_add2'),
    path('<int:pk>/edit/', v.ProdutoUpdate.as_view(), name='produto_edit'),
    path('<int:pk>/json/', v.produto_json, name='produto_json'),
    path('export/xlsx/', v.exportar_produtos_xlsx, name='export_xlsx'),
    ####Links Categoria#####
    path('categorias/',v.CategoriaListView.as_view(),name='categorias'),
    path('adicionar/categoria/', v.CategoriaCreateView.as_view(), name='categoria_add'),
    path('atualizar/categoria/<int:pk>/',v.CategoriaUpdateView.as_view(),name='update_categoria'),
]
