from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    """
    Usuário customizado do Nexus PI.
    Herda tudo do Django (login, hash de senha, admin) e adiciona o papel.
    """
    PAPEIS = [
        ('admin', 'Administrador'),
        ('coordenador', 'Coordenador'),
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
    ]
    papel = models.CharField(max_length=20, choices=PAPEIS, default='aluno')
    bio = models.TextField(blank=True, null=True, verbose_name="Biografia")

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_papel_display()})"

    @property
    def is_admin_ou_coord(self):
        return self.papel in ['admin', 'coordenador']

    @property
    def is_professor(self):
        return self.papel == 'professor'


class Projeto(models.Model):
    """
    Projeto Integrador submetido por um aluno.
    """
    STATUS_CHOICES = [
        ('desenvolvimento', 'Em Desenvolvimento'),
        ('concluido', 'Concluído'),
        ('avaliado', 'Avaliado'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    tecnologias = models.CharField(max_length=300, blank=True, verbose_name="Tecnologias")
    link_github = models.URLField(blank=True, verbose_name="Link do GitHub")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='desenvolvimento')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='projetos')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.titulo

    def get_tecnologias_lista(self):
        return [t.strip() for t in self.tecnologias.split(',') if t.strip()]

    @property
    def status_cor(self):
        cores = {
            'desenvolvimento': 'info',
            'concluido': 'success',
            'avaliado': 'warning',
        }
        return cores.get(self.status, 'secondary')
