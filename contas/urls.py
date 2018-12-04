from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.pagina_usuario, name='pagina_usuario'),
    url(r'^login-usuario/$', views.login_usuario, name='login_usuario'),
    url(r'^novo-usuario/$', views.novo_usuario, name='novo_usuario'),
    url(r'^reset-senha/$', views.reset_senha, name='reset_senha'),

    url(r'^reset-senha-confirmacao/(?P<key>\w+)/$', views.reset_senha_confirmacao, name='reset_senha_confirmacao'),

    url(r'^logout-usuario/$', views.logout_usuario, name='logout_usuario'),
    url(r'^alterar-senha/$', views.alterar_senha, name='alterar_senha'),
    url(r'^editar-cadastro/$', views.editar_cadastro, name='editar_cadastro'),
]
