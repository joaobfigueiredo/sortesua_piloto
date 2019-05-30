from django.shortcuts import render
from sortesua.models import Aposta

def aposta_index(request):
    apostas = Aposta.objects.all()
    context = {
        "apostas": apostas,
    }
    return render(request, "aposta_index.html", context)