from django.urls import path
from . import views

urlpatterns = [
	path('pac/',views.TotalList.as_view(),name="api")
]


