from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tab_2020_candidato

# Create your views here.


def index_politico(request):
    return HttpResponse('Área reservada')


def resultado_politico(request):
    return render(
        request,
        'apppolitico/principal.html', {
            # Vazio
        })


def listar_politico(request):
    db_2020_candidato = Tab_2020_candidato.objects.all()
    return render(
        request,
        'apppolitico/listar_2020_candidato.html', {
            'html_2020_candidato': db_2020_candidato
        }
    )


def atualizar_politico(request, id_politico):
    try:
        # perceba que receberá o id_politico
        db_2020_candidato = Tab_2020_candidato.objects.get(id=id_politico)
        return render(
            request, 'apppolitico/atualizar_politico.html', {
                'html_2020_candidato': db_2020_candidato
            }
        )
    except Tab_2020_candidato.DoesNotExist as e:
        return HttpResponseRedirect('/politico/listar')
