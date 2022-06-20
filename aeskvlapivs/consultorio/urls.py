from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacientes, name='pacientes'),
    path('<int:page_id>/<slug:page_slug>/', views.paciente, name='paciente'),
]




