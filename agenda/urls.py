from django.urls import path
from agenda import views

urlpatterns = [
	path('agendas/',views.agendamento,name='agendas'),
	path('adicionar/agenda/',views.AgendaCreateView.as_view(),name='add_agenda'),
	path('atualizar/agenda/<int:pk>/',views.AgendaUpdateView.as_view(),name='update_agenda'),
	path('deletar/agenda/<int:pk>/',views.AgendaDeleteView.as_view(),name='deletar_agenda'),
	path('agendas/detalhe/<int:pk>/detalhe/',views.Agenda_detalhe,name="agenda_detalhe"),
	path('status/agenda/<int:pk>/',views.AgendaStatusView.as_view(),name='agenda_status'),
]