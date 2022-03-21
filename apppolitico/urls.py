from django.urls import path
from . import views

# /politico/olamundo
# /politico/
urlpatterns = [
    path(
        '',
        views.index_politico,
        name='index_politico'
    ),
    path(
        'resultado',
        views.resultado_politico,
        name='resultado_politico'
    ),
    path(
        'listar',
        views.listar_politico,
        name='listar_politico'
    ),
    path(
        '<int:id_politico>',
        views.atualizar_politico,
        name='atualizar_politico'
    )
]
