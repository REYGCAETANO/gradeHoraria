from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib import messages
from django.contrib.auth.forms import (PasswordChangeForm, PasswordResetForm, SetPasswordForm)
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User

from .forms import NovoUsuarioForm, EditarCadastroForm, ResertSenhaForm
from .models import PasswordReset


@login_required
def novo_usuario(request):
    template_name = 'contas/novo_usuarioo.html'
    if request.method == 'POST':
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('novo_usuario')
        else:
            messages.warning(request, 'Por favor, corrija os erros abaixo!')
    else:
        form = NovoUsuarioForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def reset_senha(request):
    template_name = 'contas/reset_senha.html'
    context = {}
    form = ResertSenhaForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
        messages.success(request, 'Link enviado para o e-mail cadastrado')
        return redirect('login_usuario')
    context['form'] = form
    return render(request, template_name, context)


def reset_senha_confirmacao(request, key):
    template_name = 'contas/reset_senha_confirmacao.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


def login_usuario(request):
    tempate_name = 'contas/login_usuario.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return render(request, tempate_name)


@login_required
def alterar_senha(request):
    template_name = 'contas/alterar_senha.html'
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('alterar_senha')
        else:
            messages.error(request, 'Não foi possível alterar a senha.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, template_name, context)


def logout_usuario(request):
    logout(request)
    return redirect('login_usuario')


@login_required
def editar_cadastro(request):
    template_name = 'contas/editar_cadastro.html'
    context = {}
    if request.method == 'POST':
        form = EditarCadastroForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditarCadastroForm(instance=request.user)
            messages.success(request, 'Cadastro alterado com sucesso!')
        else:
            messages.error(request, 'Erro ao alterar os dados!')
    else:
        form = EditarCadastroForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, template_name, context)
