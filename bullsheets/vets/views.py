from django.shortcuts import render

# Create your views here.


def list_vets(request):
    return render(request, "vets/list_vets.html")
