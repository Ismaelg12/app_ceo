from django.urls import path
from pacientes import views


urlpatterns = [
	path('pacientes/',views.PacienteListView.as_view(),name='lista_pacientes'),
	path('adicionar/paciente',views.PacienteCreateView.as_view(),name='add_paciente'),
	path('atualizar/paciente/<str:pk>',views.PacienteUpdateView.as_view(),name='update_paciente'),
	path('detalhe/paciente/<str:pk>',views.PacienteDetailView,name='paciente_detalhe'),
	path('deletar/paciente/<str:pk>',views.PacienteDeleteView,name='delete_paciente'),
	path('historico/paciente/<str:pk>',views.paciente_historico,name='historico'),


]


