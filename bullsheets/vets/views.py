from django.shortcuts import render

# Create your views here.
from . import models

def list_vets(request):
    vets = models.Vet.objects.all()
    return render(request, "vets/list_vets.html", {"vets" : vets})


def vet_detail(request, pk):
    vet = models.Vet.objects.get(pk=pk)
    return render(request, "vets/vet_detail.html", {"vet" : vet})
