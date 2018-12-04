from django.contrib import admin

from .models import Disciplina, Professor, Disponibilidade, Turno, Dias, Turma

class DisciplinaAdmin(admin.ModelAdmin):

    list_display = []
    search_fields = []


class ProfessorAdmin(admin.ModelAdmin):

    list_display = ['id_professor', 'nm_professor', 'matricula']
    #search_fields = []


# class TurnoAdmin(admin.ModelAdmin):
#
#     list_display = ['cd_turno', 'qtd_aulas_dia']
#     search_fields = ['cd_turno']


# Register your models here.


admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turno)
admin.site.register(Dias)
admin.site.register(Disponibilidade)
admin.site.register(Turma)

