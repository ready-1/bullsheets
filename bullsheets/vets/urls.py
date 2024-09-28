
from django.urls import path

from . import views as vets

urlpatterns = [
    path("vets", vets.list_vets, name="list_vets"),
]
