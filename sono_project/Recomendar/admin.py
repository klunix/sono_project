from django.contrib import admin
from .models import DadosDePessoasModel

# Register your models here.
class DadosDePessoasAdmin(admin.ModelAdmin):
    pass

admin.site.register(DadosDePessoasModel,DadosDePessoasAdmin)