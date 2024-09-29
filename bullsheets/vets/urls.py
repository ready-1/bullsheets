
from django.urls import path

from . import views as vets

app_name = "vets"

urlpatterns = [
    path("vets", vets.list_vets, name="list_vets"),
    path("vet/<int:pk>", vets.vet_detail, name="vet_detail"),
]
