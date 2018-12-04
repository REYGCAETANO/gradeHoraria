from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#bibliotecas da aplicação
from .forms import DisciplinaForm, CursoForm, TurmaForm, ProfessorForm, GradeForm, TurnoForm, DisponibilidadeForm, SemestreForm
from .models import Grade, Disciplina, Curso, Professor, Disponibilidade, Turma, Turno, Semestre

#TODO: Definir a base dos templates para a pasta templates da raiz do projeto
#TODO: Refatorar as view do CRUD para usar CBV.
#TODO: Refatorar a template principal em blocos.
#TODO: Refatorar os templates para usar includes(arquivos menores)


@login_required
def index(request):
    disciplinas = Disciplina.objects.all()
    context = {
        'disciplinas': disciplinas
    }
    return render(request, 'grades/lista_disciplinas.html', context)


@login_required
def nova_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Disciplina cadastrada com sucesso!')
            return redirect('lista_disciplinas')
        else:
            messages.error(request, 'Erro ao cadastrar disciplina!')
    else:
        if request.user.is_staff:
            form = DisciplinaForm()
            return render(request, 'grades/nova_disciplina.html', {'form': form})
        else:
            messages.error(request, 'Usuário sem permissão para cadastrar disciplinas!')
            return redirect('/')


@login_required
def lista_disciplina(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'grades/lista_disciplinas.html', {'disciplinas': disciplinas})


# FIXME: Criar confirmação de exclusão antes de persistir no banco
@login_required
def deleta_disciplina(request, idDisciplina):
    if request.user.is_staff:
        deleteDisciplina = Disciplina.objects.get(id_disciplina=idDisciplina).delete()
        messages.success(request, 'Disciplina excluída com sucesso!')
    else:
        messages.error(request, 'Você não pode excluir disciplinas.')
        return render(request, 'grades/index.html')
    return redirect('lista_disciplinas')


@login_required
def editar_disciplina(request, idDisciplina):
    editar_disciplina = get_object_or_404(Disciplina, id_disciplina=idDisciplina)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=editar_disciplina)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados da disciplina alterados com sucesso!')
            return redirect('lista_disciplinas')
        else:
            messages.error(request, 'Erro ao alterar dados da disciplina')
    else:
        form = DisciplinaForm(instance=editar_disciplina)
        return render(request, 'grades/editar_disciplina.html', {'form': form})


@login_required
def novo_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso cadastrado com sucesso!')
            return redirect('lista_cursos')
        else:
            messages.error(request, 'Erro ao cadastrar o curso!')
    else:
        form = CursoForm()
    return render(request, 'grades/novo_curso.html', {'form': form})


@login_required
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'grades/lista_cursos.html', {'cursos': cursos})


# FIXME: Criar confirmção de exclusão antes de persistir no banco
@login_required
def deleta_curso(request, idCurso):
    deleteCurso = Curso.objects.get(id_curso=idCurso).delete()
    messages.success(request, 'Curso excluído com sucesso!')
    return redirect('lista_cursos')


@login_required
def editar_curso(request, idCurso):
    editarCurso = get_object_or_404(Curso, id_curso=idCurso)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=editarCurso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados do curso alterados com sucesso!')
            return redirect('lista_cursos')
        else:
            messages.error(request, 'Erro ao alterar dados do curso!')
    else:
        form = CursoForm(instance=editarCurso)
        return render(request, 'grades/editar_curso.html', {'form': form})

@login_required
def nova_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Turma cadastrada com sucesso!')
            return redirect('lista_turma')
        else:
            messages.error(request, 'Erro ao cadastrar turma!')
    else:
        form = TurmaForm()
    return render(request, 'grades/nova_turma.html', {'form': form})


@login_required
def lista_turma(request):
    turmas = Turma.objects.all()
    return render(request, 'grades/lista_turma.html', {'turmas': turmas})


# FIXME: Criar confirmação de exclusão antes de persistir no banco
@login_required
def deleta_turma(request, idTurma):
    deleteTurma = Turma.objects.get(id_turma=idTurma).delete()
    messages.success(request, 'Turma excluida com sucesso!')
    return redirect('lista_turma')


@login_required
def editar_turma(request, idTurma):
    editar_turma = get_object_or_404(Turma, id_turma=idTurma)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=editar_turma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados do turma alterados com sucesso!')
            return redirect('lista_turma')
        else:
            messages.error(request, 'Erro ao alterar dados da turma')
    else:
        form = TurmaForm(instance=editar_turma)
        return render(request, 'grades/editar_turma.html', {'form': form})


@login_required
def nova_disponibilidade(request):
    if request.method == 'POST':
        form = DisponibilidadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Disponibilidade cadastrada com sucesso!')
            return redirect('lista_disponibilidade')
        else:
            messages.error(request, 'Erro ao cadastrar nova disponibilidade!')
    else:
        form = DisponibilidadeForm
    return render(request, 'grades/nova_disponibilidade.html', {'form': form})


@login_required
def lista_disponibilidade(request):
    disponibilidades = Disponibilidade.objects.prefetch_related('dias_semana').all

    return render(request, 'grades/lista_disponibilidade.html', {'disponibilidades': disponibilidades})


@login_required
def editar_indisponibilidade(request, idIndisponibilidade):
    editar_indisponiblidade = get_object_or_404(Disponibilidade, id_indisponibilidade=idIndisponibilidade)
    if request.method == 'POST':
        form = DisponibilidadeForm(request.POST, instance=editar_indisponiblidade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Indisponibilidade alterada com sucesso!')
            return redirect('lista_disponibilidade')
        else:
            messages.error(request, 'Erro ao alterar dados da indispobilidade')
    else:
        form = DisponibilidadeForm(instance=editar_indisponiblidade)
        return render(request, 'grades/editar_indisponibilidade.html', {'form': form})


# FIXME: Criar confirmação de exclusão antes de persistir no banco
@login_required
def deleta_indisponibilidade(request, idIndisponibilidade):
    deleteIndisponbilidade = Disponibilidade.objects.get(id_indisponibilidade=idIndisponibilidade).delete()
    messages.success(request, 'Indisponibilidade excluída com sucesso!')
    return redirect('lista_disponibilidade')


@login_required
def novo_professor(request):
    template_name = 'grades/novo_professor.html'
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Professor cadastrado com sucesso!')
            return redirect('lista_professor')
        else:
            messages.warning(request, 'Erro ao cadastrar novo professor!')
    else:
        form = ProfessorForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def lista_professor(request):
    professores = Professor.objects.all().prefetch_related('disciplinas')
    return render(request, 'grades/lista_professor.html', {'professores': professores})


@login_required
def editar_professor(request, idProfessor):
    editar_professor = get_object_or_404(Professor, id_professor=idProfessor)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=editar_professor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados do professor alterados com sucesso!')
            return redirect('lista_professor')
        else:
            messages.error(request, 'Erro ao alterar dados do professor')
    else:
        form = ProfessorForm(instance=editar_professor)
        return render(request, 'grades/editar_professor.html', {'form': form})


# FIXME: Criar confirmação de exclusão antes de persistir no banco
@login_required
def deleta_professor(request, idProfessor):
    template_name = 'grades/detete.html'
    deleteProfessor = Professor.objects.get(id_professor=idProfessor).delete()
    messages.warning(request, 'Professor excluído com sucesso!')
    return redirect('lista_professor')


@login_required
def nova_grade(request):
    template_name = 'grades/nova_grade.html'
    contexto = {}
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Grade gerada com sucesso!')
            return redirect('lista_grades')
        else:
            messages.error(request, 'Erro ao gerar a grade!')
    else:
        form = GradeForm()
        contexto['form'] = form
    return render(request, template_name, contexto)


@login_required
def lista_grades(request):
    grades = Grade.objects.all()
    return render(request, 'grades/lista_grades.html', {'grades': grades})


@login_required
def novo_turno(request):
    template_name = 'grades/novo_turno.html'
    contexto = {}
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Turno cadastrado com sucesso!')
            return redirect('lista_grades')
        else:
            messages.error(request, 'Erro ao cadastar turno!')
    else:
        turno = Turno.objects.all()
        contexto['turno'] = turno
        form = TurnoForm()
        contexto['form'] = form
    return render(request, template_name, contexto)


def editar_turno(request, idTurno):
    editarTurno = get_object_or_404(Turno, id_turno=idTurno)
    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=editarTurno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados do turno alterados com sucesso!')
            return redirect('lista_turno')
        else:
            messages.error(request, 'Erro ao alterar dados do turno!')
    else:
        form = TurnoForm(instance=editarTurno)
        return render(request, 'grades/editar_turno.html', {'form': form})


@login_required
def lista_turno(request):
    # import pdb; pdb.set_trace()
    turno = Turno.objects.prefetch_related('dias').all()
    # print(f'Dias {turno.dias[0]}, turno: {turno}')
    return render(request, 'grades/lista_turno.html', {'turno': turno})


@login_required
def novo_semestre(request):
    template_name = 'grades/novo_semestre.html'
    if request.method == 'POST':
        form = SemestreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Semestre cadastrado com sucesso!')
            return redirect('/')
        else:
            messages.warning(request, 'Erro ao cadastrar novo semestre!')
    else:
        form = SemestreForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
