from django.urls import path
from . import views

urlpatterns = [
    path("treino/", views.ListarTreinamento.as_view(), name="sonia_train_index"),
    path("treino/create", views.CriarTreinamento.as_view(), name="sonia_train_create")
]
