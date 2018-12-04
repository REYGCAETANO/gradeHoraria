from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from grades.mail import send_mail_template
from grades.utils import generate_hash_key

from .models import PasswordReset

User = get_user_model()


# class UserForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('first_name', 'last_name', 'username',  'email', 'password')


class ResertSenhaForm(forms.Form):
    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Nenhum usuário encontrado com este e-mail')

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'contas/reset_senha_mail.html'
        subject = 'Criar nova senha do sistema GradeExata'
        context = {
            'reset': reset,
        }
        send_mail_template(subject, template_name, context, [user.email])


class NovoUsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label='Nome')
    last_name = forms.CharField(max_length=50, label='Sobrenome')
    email = forms.EmailField(label='E-mail')

    def clean_email(self):

        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe um usuário com este e-mail')
        return email

    def save(self, commit=True):
        user = super(NovoUsuarioForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EditarCadastroForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Já existe um usuário com este e-mail')
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
