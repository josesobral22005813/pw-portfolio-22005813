from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Competencia)
admin.site.register(Projeto)
admin.site.register(Cadeira)
admin.site.register(PontuacaoQuizz)