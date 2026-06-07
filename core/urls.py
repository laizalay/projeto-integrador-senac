from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('painel/', views.painel, name='painel'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('portfolio/', views.portfolio_publico, name='portfolio'),

    # CRUD Projetos
    path('projeto/novo/', views.projeto_novo, name='projeto_novo'),
    path('projeto/<int:pk>/', views.projeto_detalhe, name='projeto_detalhe'),
    path('projeto/<int:pk>/editar/', views.projeto_editar, name='projeto_editar'),
    path('projeto/<int:pk>/excluir/', views.projeto_excluir, name='projeto_excluir'),
    path('projeto/<int:pk>/avaliar/', views.projeto_avaliar, name='projeto_avaliar'),

    # Usuários
    path('usuarios/', views.usuarios_lista, name='usuarios'),
    path('usuarios/novo/', views.usuario_novo, name='usuario_novo'),
    path('usuarios/<int:pk>/editar/', views.usuario_editar, name='usuario_editar'),
    path('usuarios/<int:pk>/senha/', views.usuario_senha, name='usuario_senha'),
]
