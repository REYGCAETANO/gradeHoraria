from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class DisciplinaFiltros(models.Manager):

    def pesquisar(self, query):
        return self.get_queryset().filter(
            models.Q(nm_disciplina__icontains=query) |
            models.Q(sigla_disciplina=query)
        )


class Grade(models.Model):
    id_grade = models.AutoField(primary_key=True)
    cd_curso = models.IntegerField()
    cd_turno = models.IntegerField()
    cd_disciplina = models.IntegerField()
    cd_turma = models.IntegerField()
    cd_professor = models.IntegerField()


class Disciplina(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    nm_disciplina = models.CharField(max_length=50, verbose_name="Descrição da Disciplina")
    sigla_disciplina = models.CharField(max_length=5, verbose_name="Sigla da Disciplina")

    def __str__(self):
        return self.nm_disciplina

    def save(self, force_insert=False, force_update=False):
        self.nm_disciplina = self.nm_disciplina.upper()
        super(Disciplina, self).save(force_insert, force_update)

    objects = DisciplinaFiltros()


# class Turno(models.Model):
#     TURNO_CHOICES = (
#         ('1', 'Matutino'),
#         ('2', 'Vespertino'),
#         ('3', 'Noturno'),
#     )
#     SEMANA_CHOICES = (
#         ('1', 'Domingo-Feira'),
#         ('2', 'Segunda-Feira'),
#         ('3', 'Terça-Feira'),
#         ('4', 'Quarta-Feira'),
#         ('5', 'Quinta-Feira'),
#         ('6', 'Sexta-Feira'),
#         ('7', 'Sábado'),
#     )
#     id_turno = models.AutoField(primary_key=True)
#     cd_turno = models.CharField(max_length=1, choices=TURNO_CHOICES, verbose_name="Turno")
#     dia_semana = models.CharField(max_length=100, choices=SEMANA_CHOICES, verbose_name="Dia da Semana")
#     qtd_aulas_dia = models.IntegerField(verbose_name='Qtd. de Aulas por dia')
#
#     def __str__(self):
#         return self.cd_turno
#
#     class Meta:
#         verbose_name = 'Turno'
#         verbose_name_plural = 'Turnos'
#         ordering = ['cd_turno']

class Dias(models.Model):
    id_dia = models.AutoField(primary_key=True)
    dia_semana = models.CharField(max_length=30, verbose_name='Dia da Semana')
    qtd_aulas_dia = models.IntegerField(null=True, blank=True, verbose_name='qtd')

    class Meta:
        unique_together = ('dia_semana',)

    def __str__(self):
        return self.dia_semana


class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True, unique=True)
    turno = models.CharField(max_length=20, verbose_name='Turno')
    dias = models.ManyToManyField(Dias, related_name='turno_dias', blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return "%s (%s)" % (self.turno, ", ".join(dia.dia_semana for dia in self.dias.all()))

    class Meta:
        unique_together = ('turno',)


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nm_curso = models.CharField(max_length=50, verbose_name="Nome do Curso")
    sigla_curso = models.CharField(max_length=5, verbose_name="Sigla do Curso")

    def __str__(self):
        return self.nm_curso

    def save(self, force_insert=False, force_update=False):
        self.nm_curso = self.nm_curso.upper()
        super(Curso, self).save(force_insert, force_update)

class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    nm_professor = models.CharField(max_length=100, verbose_name='Nome')
    matricula = models.CharField(max_length=50, verbose_name='Matrícula')
    disciplinas = models.ManyToManyField(Disciplina, related_name='professor_disciplina', verbose_name='Disciplina')
    turnos = models.ManyToManyField(Turno, related_name='professor_turno', verbose_name='Turno')

    def save(self, force_insert=False, force_update=False):
        self.nm_professor = self.nm_professor.upper()
        super(Professor, self).save(force_insert, force_update)
    # def __str__(self):
    #     return self.nm_professor

    def __str__(self):
        return "%s (%s)" % (self.nm_professor, ", ".join(disciplina.nm_disciplina for disciplina in self.disciplinas.all()))

    class Meta:
        unique_together = ('matricula',)


class Disponibilidade(models.Model):
    id_indisponibilidade = models.AutoField(primary_key=True)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, blank=False, related_name='disponibilidade_turno')
    dias_semana = models.ManyToManyField(Dias, blank=False, related_name='disponibilidade_dias')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='disponibilidade_professor', null=True, blank=False)

    def __str__(self):  # __unicode__ on Python 2
        return "(%s)" % (", ".join(dias.dia_semana for dias in self.dias_semana.all()))

    class Meta:
        unique_together = ('professor',)

class Semestre(models.Model):
    Semestre1 = 1
    Semestre2 = 2
    Semestre3 = 3
    Semestre4 = 4
    Semestre5 = 5
    Semestre6 = 6
    Semestre7 = 7
    Semestre8 = 8
    Semestre9 = 9
    Semestre10 = 10

    SEMESTRE_CHOICES = (
        (Semestre1, '1º Semestre'),
        (Semestre2, '2º Semestre'),
        (Semestre3, '3º Semestre'),
        (Semestre4, '4º Semestre'),
        (Semestre5, '5º Semestre'),
        (Semestre6, '6º Semestre'),
        (Semestre7, '7º Semestre'),
        (Semestre8, '8º Semestre'),
        (Semestre9, '9º Semestre'),
        (Semestre10, '10ºSemestre'),
    )
    id_semestre = models.AutoField(primary_key=True)
    semestre = models.IntegerField(choices=SEMESTRE_CHOICES, verbose_name="SEMESTRE")
    # cd_curso = models.IntegerField(Curso)
    cd_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    cd_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name='Turno')
    #cd_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    aula_semana = models.ManyToManyField(Dias, related_name='semestre_dias', verbose_name='Dia da semana')

    def __str__(self):  # __unicode__ on Python 2
        return "%s" % (self.get_semestre_display())

    class Meta:
        ordering = ["semestre"]


class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)
    ds_turma = models.CharField(max_length=20, verbose_name='Descrição da Turma', unique=True)
    cd_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    cd_semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, verbose_name='Semestre')
    cd_disciplinas = models.ManyToManyField(Disciplina, blank=False, verbose_name='Disciplinas')
    cd_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='turma_professor', verbose_name='Professor')

    def __str__(self):
        return self.ds_turma

    def save(self, force_insert=False, force_update=False):
        self.ds_turma = self.ds_turma.upper()
        super(Turma, self).save(force_insert, force_update)
    # class Meta:
    #     unique_together = ('ds_turma',)
