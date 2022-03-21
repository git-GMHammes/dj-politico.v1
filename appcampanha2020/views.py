from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import tap_app

# Create your views here.

def listar_politico(request):
    db_campanha2020 = tab__.objects.all()
    return render(
        request,
        'appcampanha2020/listar_campanha2020.html', {
            'html_campanha2020': db_campanha2020
        }
    )
