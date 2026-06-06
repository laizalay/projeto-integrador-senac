from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from functools import wraps
from .models import Usuario, Projeto
from .forms import LoginForm, UsuarioForm, ProjetoForm


# ─── DECORADORES ───
def admin_ou_coord(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_admin_ou_coord:
            messages.error(request, 'Acesso restrito a administradores e coordenadores.')
            return redirect('painel')
        return f(request, *args, **kwargs)
    return decorated


# ─── PÚBLICAS ───
def home(request):
    total_projetos = Projeto.objects.count()
    total_alunos = Usuario.objects.filter(papel='aluno').count()
    projetos_recentes = Projeto.objects.select_related('autor').order_by('-criado_em')[:4]
    return render(request, 'home.html', {
        'total_projetos': total_projetos,
        'total_alunos': total_alunos,
        'projetos_recentes': projetos_recentes,
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('painel')
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f'Bem-vindo(a), {user.first_name or user.username}!')
        return redirect('painel')
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('home')


# ─── PAINEL ───
@login_required
def painel(request):
    usuario = request.user
    if usuario.is_admin_ou_coord or usuario.is_professor:
        projetos = Projeto.objects.select_related('autor').all()
    else:
        projetos = Projeto.objects.filter(autor=usuario)

    # Stats para o painel
    stats = {
        'total': projetos.count(),
        'desenvolvimento': projetos.filter(status='desenvolvimento').count(),
        'concluido': projetos.filter(status='concluido').count(),
        'avaliado': projetos.filter(status='avaliado').count(),
    }
    return render(request, 'painel.html', {'projetos': projetos, 'stats': stats})


# ─── CRUD PROJETOS ───
@login_required
def projeto_novo(request):
    form = ProjetoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        projeto = form.save(commit=False)
        projeto.autor = request.user
        projeto.save()
        messages.success(request, 'Projeto submetido com sucesso!')
        return redirect('painel')
    return render(request, 'projeto_form.html', {'form': form, 'acao': 'Novo'})


@login_required
def projeto_detalhe(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if projeto.autor != request.user and not request.user.is_admin_ou_coord:
        messages.error(request, 'Você não tem permissão para ver este projeto.')
        return redirect('painel')
    return render(request, 'projeto_detalhe.html', {'projeto': projeto})


@login_required
def projeto_editar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if projeto.autor != request.user and not request.user.is_admin_ou_coord:
        messages.error(request, 'Você não tem permissão para editar este projeto.')
        return redirect('painel')
    form = ProjetoForm(request.POST or None, instance=projeto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Projeto atualizado com sucesso!')
        return redirect('painel')
    return render(request, 'projeto_form.html', {'form': form, 'acao': 'Editar', 'projeto': projeto})


@login_required
def projeto_excluir(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if projeto.autor != request.user and not request.user.is_admin_ou_coord:
        messages.error(request, 'Você não tem permissão para excluir este projeto.')
        return redirect('painel')
    if request.method == 'POST':
        projeto.delete()
        messages.info(request, 'Projeto excluído.')
        return redirect('painel')
    return render(request, 'projeto_confirmar_exclusao.html', {'projeto': projeto})


# ─── USUÁRIOS ───
@admin_ou_coord
def usuarios_lista(request):
    usuarios = Usuario.objects.all().order_by('-date_joined')
    return render(request, 'usuarios.html', {'usuarios': usuarios})


@admin_ou_coord
def usuario_novo(request):
    form = UsuarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Usuário cadastrado com sucesso!')
        return redirect('usuarios')
    return render(request, 'usuario_form.html', {'form': form})
