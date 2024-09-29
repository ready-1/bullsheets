from django.shortcuts import render, redirect

# Create your views here.
from . import models
from .forms import VetForm


def list_vets(request):
    vets = models.Vet.objects.all()
    return render(request, "vets/list_vets.html", {"vets": vets})


def vet_detail(request, pk):
    vet = models.Vet.objects.get(pk=pk)
    return render(request, "vets/vet_detail.html", {"vet": vet})


def new_vet(request):
    if request.method == "POST":
        form = VetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vets:list_vets")
    else:
        form = VetForm()
    return render(request, "vets/vet_form.html", {"form": form})

def edit_vet(request, pk):
    if request.method == "POST":
        vet = models.Vet.objects.get(pk=pk)
        form = VetForm(request.POST, instance=vet)
        if form.is_valid():
            form.save()
            return redirect("vets:list_vets")
    else:
        vet = models.Vet.objects.get(pk=pk)
        form = VetForm(instance=vet)
    return render(request, "vets/vet_form.html", {"form": form})


def delete_vet(request, pk):
    models.Vet.objects.get(pk=pk).delete()
    return redirect("vets:list_vets")
