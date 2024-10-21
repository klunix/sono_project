from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tirescue-home'),
    path('informar/', views.informar_problema, name='tirescue-info-problema'),
    path('deletar/<int:problema_id>/', views.deletar_problema, name='tirescue-del-problema'),
]
