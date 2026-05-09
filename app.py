from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'senac-observatorio-2025')

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
os.makedirs(INSTANCE_DIR, exist_ok=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(INSTANCE_DIR, 'observatorio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ─────────────────────────────────────────
# MODELOS (tabelas do banco de dados)
# ─────────────────────────────────────────

class Usuario(db.Model):
    """
    Representa um usuário do sistema.
    Papéis possíveis: 'admin', 'coordenador', 'aluno'
    """
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    papel = db.Column(db.String(20), nullable=False, default='aluno')  # admin | coordenador | aluno
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    projetos = db.relationship('Projeto', backref='autor', lazy=True)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)


class Projeto(db.Model):
    """
    Representa um projeto integrador submetido por um aluno.
    """
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    tecnologias = db.Column(db.String(300))
    link_github = db.Column(db.String(300))
    status = db.Column(db.String(30), default='Em desenvolvimento')  # Em desenvolvimento | Concluído | Avaliado
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)


# ─────────────────────────────────────────
# DECORADORES (proteção de rotas)
# ─────────────────────────────────────────

def login_required(f):
    """Garante que o usuário está logado para acessar a rota."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('Faça login para continuar.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


def admin_ou_coord_required(f):
    """Garante que apenas Admin ou Coordenador acessem a rota."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('login'))
        usuario = db.session.get(Usuario, session['usuario_id'])
        if usuario.papel not in ['admin', 'coordenador']:
            flash('Acesso restrito a administradores e coordenadores.', 'danger')
            return redirect(url_for('painel'))
        return f(*args, **kwargs)
    return decorated


# ─────────────────────────────────────────
# ROTAS PÚBLICAS
# ─────────────────────────────────────────

@app.route('/')
def home():
    """Página inicial do sistema."""
    total_projetos = Projeto.query.count()
    total_alunos = Usuario.query.filter_by(papel='aluno').count()
    projetos_recentes = Projeto.query.order_by(Projeto.criado_em.desc()).limit(3).all()
    return render_template('home.html',
                           total_projetos=total_projetos,
                           total_alunos=total_alunos,
                           projetos_recentes=projetos_recentes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Tela de login."""
    if 'usuario_id' in session:
        return redirect(url_for('painel'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '')
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.check_senha(senha):
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            session['usuario_papel'] = usuario.papel
            flash(f'Bem-vindo(a), {usuario.nome}!', 'success')
            return redirect(url_for('painel'))
        else:
            flash('E-mail ou senha incorretos.', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('home'))


# ─────────────────────────────────────────
# PAINEL DO ALUNO (CRUD de Projetos)
# ─────────────────────────────────────────

@app.route('/painel')
@login_required
def painel():
    """Painel principal - lista os projetos do aluno logado."""
    usuario = db.session.get(Usuario, session['usuario_id'])
    # Admin e coordenador veem todos os projetos; aluno vê apenas os seus
    if usuario.papel in ['admin', 'coordenador']:
        projetos = Projeto.query.order_by(Projeto.criado_em.desc()).all()
    else:
        projetos = Projeto.query.filter_by(usuario_id=usuario.id)\
                                .order_by(Projeto.criado_em.desc()).all()
    return render_template('painel.html', usuario=usuario, projetos=projetos)


@app.route('/projeto/novo', methods=['GET', 'POST'])
@login_required
def novo_projeto():
    """CREATE — Submeter um novo projeto."""
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        descricao = request.form.get('descricao', '').strip()
        tecnologias = request.form.get('tecnologias', '').strip()
        link_github = request.form.get('link_github', '').strip()

        if not titulo or not descricao:
            flash('Título e descrição são obrigatórios.', 'warning')
        else:
            projeto = Projeto(
                titulo=titulo,
                descricao=descricao,
                tecnologias=tecnologias,
                link_github=link_github,
                usuario_id=session['usuario_id']
            )
            db.session.add(projeto)
            db.session.commit()
            flash('Projeto submetido com sucesso!', 'success')
            return redirect(url_for('painel'))

    return render_template('projeto_form.html', projeto=None, acao='Novo')


@app.route('/projeto/<int:id>')
@login_required
def ver_projeto(id):
    """READ — Visualizar detalhes de um projeto."""
    projeto = db.get_or_404(Projeto, id)
    usuario = db.session.get(Usuario, session['usuario_id'])
    # Só o dono ou admin/coord pode ver
    if projeto.usuario_id != usuario.id and usuario.papel not in ['admin', 'coordenador']:
        flash('Você não tem permissão para ver este projeto.', 'danger')
        return redirect(url_for('painel'))
    return render_template('projeto_detalhe.html', projeto=projeto)


@app.route('/projeto/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_projeto(id):
    """UPDATE — Editar/atualizar um projeto."""
    projeto = db.get_or_404(Projeto, id)
    usuario = db.session.get(Usuario, session['usuario_id'])

    if projeto.usuario_id != usuario.id and usuario.papel not in ['admin', 'coordenador']:
        flash('Você não tem permissão para editar este projeto.', 'danger')
        return redirect(url_for('painel'))

    if request.method == 'POST':
        projeto.titulo = request.form.get('titulo', '').strip()
        projeto.descricao = request.form.get('descricao', '').strip()
        projeto.tecnologias = request.form.get('tecnologias', '').strip()
        projeto.link_github = request.form.get('link_github', '').strip()
        projeto.status = request.form.get('status', 'Em desenvolvimento')
        projeto.atualizado_em = datetime.utcnow()
        db.session.commit()
        flash('Projeto atualizado com sucesso!', 'success')
        return redirect(url_for('painel'))

    return render_template('projeto_form.html', projeto=projeto, acao='Editar')


@app.route('/projeto/<int:id>/excluir', methods=['POST'])
@login_required
def excluir_projeto(id):
    """DELETE — Excluir um projeto."""
    projeto = db.get_or_404(Projeto, id)
    usuario = db.session.get(Usuario, session['usuario_id'])

    if projeto.usuario_id != usuario.id and usuario.papel not in ['admin', 'coordenador']:
        flash('Você não tem permissão para excluir este projeto.', 'danger')
        return redirect(url_for('painel'))

    db.session.delete(projeto)
    db.session.commit()
    flash('Projeto excluído.', 'info')
    return redirect(url_for('painel'))


# ─────────────────────────────────────────
# GESTÃO DE USUÁRIOS (Admin/Coordenador)
# ─────────────────────────────────────────

@app.route('/usuarios')
@admin_ou_coord_required
def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    usuarios = Usuario.query.order_by(Usuario.criado_em.desc()).all()
    return render_template('usuarios.html', usuarios=usuarios)


@app.route('/usuarios/novo', methods=['GET', 'POST'])
@admin_ou_coord_required
def novo_usuario():
    """Cadastro de novo usuário (apenas Admin/Coordenador)."""
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '')
        papel = request.form.get('papel', 'aluno')

        if Usuario.query.filter_by(email=email).first():
            flash('Este e-mail já está cadastrado.', 'warning')
        elif not nome or not email or not senha:
            flash('Todos os campos são obrigatórios.', 'warning')
        else:
            usuario = Usuario(nome=nome, email=email, papel=papel)
            usuario.set_senha(senha)
            db.session.add(usuario)
            db.session.commit()
            flash(f'Usuário {nome} cadastrado com sucesso!', 'success')
            return redirect(url_for('listar_usuarios'))

    return render_template('usuario_form.html')


# ─────────────────────────────────────────
# INICIALIZAÇÃO
# ─────────────────────────────────────────


@app.before_request
def inicializar():
    """Cria as tabelas e o admin antes da primeira requisição."""
    db.create_all()
    if not Usuario.query.first():
        admin = Usuario(nome='Administrador', email='admin@senac.br', papel='admin')
        admin.set_senha('admin123')
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
