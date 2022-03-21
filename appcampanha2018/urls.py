from django.urls import path
from . import views

urlpatterns = [
    path('listar', views.listar_campanha2018, name='listar_campanha2018'),
]