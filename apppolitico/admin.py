from django.contrib import admin
from .models import Tab_partido_politico, Tab_2020_candidato
# Register your models here.

class ApppoliticoAdmin(admin.ModelAdmin): # vai para register
    list_display = (
        'id', 
        'str_nome_votavel',
        'int_numero_votavel',
        'str_partido_politico',
        'str_desc_cargo',
        'int_qtd_votos',
        'str_situacao'
    )
    list_filter = (
        'str_partido_politico', 
        'str_situacao'
    )
    list_per_page = 10
    search_fields = (
        'str_nome_votavel', 
        'str_desc_cargo'
    )

admin.site.register(
    Tab_partido_politico
    )
admin.site.register(
    Tab_2020_candidato,
    ApppoliticoAdmin # A Classe acima
)
