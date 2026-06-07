from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Avg
from functools import wraps
from .models import Usuario, Projeto, Avaliacao
from .forms import LoginForm, UsuarioForm, UsuarioEditarForm, ProjetoForm, AvaliacaoForm


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


def so_admin(f):
    """Apenas Administrador acessa — manutenção técnica."""
    @wraps(f)
    def decorated(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.papel != 'admin':
            messages.error(request, 'Acesso restrito ao Administrador.')
            return redirect('painel')
        return f(request, *args, **kwargs)
    return decorated


def professor_required(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_professor and not request.user.is_admin_ou_coord:
            messages.error(request, 'Acesso restrito a professores.')
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


def portfolio_publico(request):
    """Página pública para empresas consultarem projetos concluídos."""
    tecnologia = request.GET.get('tech', '')
    turma = request.GET.get('turma', '')
    projetos = Projeto.objects.filter(status__in=['concluido', 'avaliado']).select_related('autor')
    if tecnologia:
        projetos = projetos.filter(tecnologias__icontains=tecnologia)
    if turma:
        projetos = projetos.filter(turma__icontains=turma)
    turmas = Projeto.objects.exclude(turma__isnull=True).exclude(turma='').values_list('turma', flat=True).distinct()
    return render(request, 'portfolio.html', {
        'projetos': projetos,
        'tecnologia': tecnologia,
        'turma': turma,
        'turmas': turmas,
        'total': projetos.count(),
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
    turma_filtro = request.GET.get('turma', '')
    status_filtro = request.GET.get('status', '')

    if usuario.is_admin_ou_coord or usuario.is_professor:
        projetos = Projeto.objects.select_related('autor').prefetch_related('avaliacoes')
    else:
        projetos = Projeto.objects.filter(autor=usuario).prefetch_related('avaliacoes')

    if turma_filtro:
        projetos = projetos.filter(turma__icontains=turma_filtro)
    if status_filtro:
        projetos = projetos.filter(status=status_filtro)

    turmas = Projeto.objects.exclude(turma__isnull=True).exclude(turma='').values_list('turma', flat=True).distinct()

    stats = {
        'total': projetos.count(),
        'desenvolvimento': projetos.filter(status='desenvolvimento').count(),
        'concluido': projetos.filter(status='concluido').count(),
        'avaliado': projetos.filter(status='avaliado').count(),
    }
    return render(request, 'painel.html', {
        'projetos': projetos,
        'stats': stats,
        'turmas': turmas,
        'turma_filtro': turma_filtro,
        'status_filtro': status_filtro,
    })


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
    if projeto.autor != request.user and not request.user.is_admin_ou_coord and not request.user.is_professor:
        messages.error(request, 'Você não tem permissão para ver este projeto.')
        return redirect('painel')
    avaliacao = projeto.avaliacoes.first()
    return render(request, 'projeto_detalhe.html', {'projeto': projeto, 'avaliacao': avaliacao})


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


# ─── AVALIAÇÃO (Professor) ───
@professor_required
def projeto_avaliar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    avaliacao_existente = projeto.avaliacoes.filter(professor=request.user).first()
    form = AvaliacaoForm(request.POST or None, instance=avaliacao_existente)
    if request.method == 'POST' and form.is_valid():
        avaliacao = form.save(commit=False)
        avaliacao.projeto = projeto
        avaliacao.professor = request.user
        avaliacao.save()
        projeto.status = 'avaliado'
        projeto.save()
        messages.success(request, f'Avaliação registrada! Média: {avaliacao.media}/10')
        return redirect('painel')
    return render(request, 'projeto_avaliar.html', {
        'form': form,
        'projeto': projeto,
        'avaliacao': avaliacao_existente,
    })


# ─── DASHBOARD COORDENADOR ───
@admin_ou_coord
def dashboard(request):
    total_projetos = Projeto.objects.count()
    total_alunos = Usuario.objects.filter(papel='aluno').count()
    total_professores = Usuario.objects.filter(papel='professor').count()
    total_avaliados = Projeto.objects.filter(status='avaliado').count()
    total_concluidos = Projeto.objects.filter(status='concluido').count()
    total_desenvolvimento = Projeto.objects.filter(status='desenvolvimento').count()

    projetos_por_turma = Projeto.objects.exclude(turma__isnull=True).exclude(turma='') \
        .values('turma').annotate(total=Count('id')).order_by('turma')

    ultimas_avaliacoes = Avaliacao.objects.select_related('professor', 'projeto') \
        .order_by('-avaliado_em')[:5]

    return render(request, 'dashboard.html', {
        'total_projetos': total_projetos,
        'total_alunos': total_alunos,
        'total_professores': total_professores,
        'total_avaliados': total_avaliados,
        'total_concluidos': total_concluidos,
        'total_desenvolvimento': total_desenvolvimento,
        'projetos_por_turma': projetos_por_turma,
        'ultimas_avaliacoes': ultimas_avaliacoes,
    })


# ─── USUÁRIOS ───
@admin_ou_coord
def usuarios_lista(request):
    usuarios = Usuario.objects.all().order_by('-date_joined')
    return render(request, 'usuarios.html', {'usuarios': usuarios})


@admin_ou_coord
def usuario_novo(request):
    form = UsuarioForm(request.POST or None, usuario_logado=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('usuarios')
    return render(request, 'usuario_form.html', {'form': form})


@admin_ou_coord
def usuario_editar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    form = UsuarioEditarForm(request.POST or None, instance=usuario)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Usuário atualizado!')
        return redirect('usuarios')
    return render(request, 'usuario_editar.html', {'form': form, 'usuario': usuario})


@so_admin
def usuario_senha(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    erro = None
    if request.method == 'POST':
        senha = request.POST.get('senha', '')
        confirma = request.POST.get('senha_confirma', '')
        if len(senha) < 6:
            erro = 'A senha deve ter pelo menos 6 caracteres.'
        elif senha != confirma:
            erro = 'As senhas não coincidem.'
        else:
            usuario.set_password(senha)
            usuario.save()
            messages.success(request, f'Senha redefinida com sucesso!')
            return redirect('usuarios')
    return render(request, 'usuario_senha.html', {'usuario': usuario, 'erro': erro})
