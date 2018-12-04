from django.conf.urls import url
from . import views

# TODO: Refatorar a repetição de urls para o mesmo propósito
# TODO: Refatorar a url para não usar mais RegEx

urlpatterns = [
    # DISCIPLINA
    url(r'nova-disciplina/$', views.nova_disciplina, name='nova_disciplina'),
    url(r'lista-disciplinas/$', views.lista_disciplina, name='lista_disciplinas'),
    # url(r'^deleta-disciplina/(?P<pk>\d+)/$', views.deleta_disciplina, name='deleta_disciplina'),
    url(r'^deleta-disciplina/(?P<idDisciplina>[0-9]+)/$', views.deleta_disciplina, name='deleta_disciplina'),
    url(r'editar-disciplina/(?P<idDisciplina>[0-9]+)/$', views.editar_disciplina, name='editar_disciplina'),
    # PROFESSOR
    url(r'novo-professor/$', views.novo_professor, name='novo_professor'),
    url(r'lista-professor/$', views.lista_professor, name='lista_professor'),
    url(r'^editar-professor/(?P<idProfessor>[0-9]+)/$', views.editar_professor, name='editar_professor'),
    url(r'^deleta-professor/(?P<idProfessor>[0-9]+)/$', views.deleta_professor, name='deleta_professor'),
    # GRADE HORÁRIA
    url(r'grade-horaria/$', views.nova_grade, name='nova_grade'),
    url(r'lista-grades/$', views.lista_grades, name='lista_grades'),
    # CURSO
    url(r'novo-curso/$', views.novo_curso, name='novo_curso'),
    url(r'lista-cursos/$', views.lista_cursos, name='lista_cursos'),
    url(r'editar-curso/(?P<idCurso>[0-9]+)/$', views.editar_curso, name='editar_curso'),
    url(r'deleta-curso/(?P<idCurso>[0-9]+)/$', views.deleta_curso, name='deleta_curso'),
    # Disponibilidade
    url(r'nova-disponibilidade/$', views.nova_disponibilidade, name='nova_disponibilidade'),
    url(r'lista-disponibilidade/$', views.lista_disponibilidade, name='lista_disponibilidade'),
    url(r'editar-indisponibilidade/(?P<idIndisponibilidade>[0-9]+)/$', views.editar_indisponibilidade, name='editar_indisponibilidade'),
    url(r'deleta-indisponibilidade/(?P<idIndisponibilidade>[0-9]+)/$', views.deleta_indisponibilidade, name='deleta_indisponibilidade'),
    # TURMA
    url(r'nova-turma/$', views.nova_turma, name='nova_turma'),
    url(r'lista-turma/$', views.lista_turma, name='lista_turma'),
    url(r'editar-turma/(?P<idTurma>[0-9]+)/$', views.editar_turma, name='editar_turma'),
    url(r'deleta-turma/(?P<idTurma>[0-9]+)/$', views.deleta_turma, name='deleta_turma'),
    # TURNO
    url(r'novo-turno/$', views.novo_turno, name='novo_turno'),
    url(r'editar-turno/(?P<idTurno>[0-9]+)/$', views.editar_turno, name='editar_turno'),
    url(r'lista-turno/$', views.lista_turno, name='lista_turno'),
    #SEMESTRE
    url(r'novo-semestre/$', views.novo_semestre, name='novo_semestre')
]
