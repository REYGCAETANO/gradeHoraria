from django import forms

from .models import Disciplina, Curso, Turno, Turma, Professor, Grade, Disponibilidade, Semestre


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


#class TurnoFormt(forms.ModelForm):
 #   class Meta:
  #      model = Turno
   #     cd_turno = forms.IntegerField
    #    dia_semana = forms.CheckboxSelectMultiple()
     #   qtd_aulas_dia = forms.IntegerField
      #  fields = ['cd_turno', 'dia_semana', 'qtd_aulas_dia']


class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'
        #exclude = ['professor_id', 'disciplina_id']


class ProfessorForm(forms.ModelForm):

    #turno = forms.CharField(label="Turno", required=True)
    #disponibilidade = forms.CharField(label="disponibilidade", required=False)

    class Meta:
        model = Professor
        #fields = ['nm_professor', 'matricula']
        fields = '__all__'


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'


class DisponibilidadeForm(forms.ModelForm):

    #disponibilidade = Turno.objects.last()
    # disponibilidade.turno

    class Meta:
        model = Disponibilidade
        fields = '__all__'
        #exclude = ['turno']

class SemestreForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = '__all__'