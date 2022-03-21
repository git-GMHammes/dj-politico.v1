from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import tap_app

# Create your views here.

def listar_politico(request):
    db_campanha2018 = tab__.objects.all()
    return render(
        request,
        'cappcampanha2018/listar_ampanha2018.html', {
            'html_campanha2018': db_campanha2018
        }
    )
