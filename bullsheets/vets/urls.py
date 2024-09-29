
from django.urls import path

from . import views as vets

app_name = "vets"

urlpatterns = [
    path("", vets.list_vets, name="list_vets"),
    path("vet/<int:pk>", vets.vet_detail, name="vet_detail"),
    path("new_vet", vets.new_vet, name="new_vet"),
    path("edit_vet/<int:pk>", vets.edit_vet, name="edit_vet"),
    path("delete_vet/<int:pk>", vets.delete_vet, name="delete_vet"),
    path("factory", vets.create_10_vets, name="vets_factory"),
]
