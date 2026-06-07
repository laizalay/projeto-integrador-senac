from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    PAPEIS = [
        ('admin', 'Administrador'),
        ('coordenador', 'Coordenador'),
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
    ]
    papel = models.CharField(max_length=20, choices=PAPEIS, default='aluno')
    bio = models.TextField(blank=True, null=True, verbose_name="Biografia")
    turma = models.CharField(max_length=50, blank=True, null=True, verbose_name="Turma")

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
    turma = models.CharField(max_length=50, blank=True, null=True, verbose_name="Turma")
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

    @property
    def avaliacao(self):
        return self.avaliacoes.first()


class Avaliacao(models.Model):
    """Avaliação de um projeto pelo professor — com rubrica."""
    NOTAS = [(i, str(i)) for i in range(0, 11)]

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='avaliacoes')
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='avaliacoes_feitas')

    # Rubrica — 4 critérios
    nota_desenvolvimento = models.IntegerField(choices=NOTAS, default=0, verbose_name="Desenvolvimento Técnico (0-10)")
    nota_documentacao = models.IntegerField(choices=NOTAS, default=0, verbose_name="Documentação (0-10)")
    nota_apresentacao = models.IntegerField(choices=NOTAS, default=0, verbose_name="Apresentação (0-10)")
    nota_inovacao = models.IntegerField(choices=NOTAS, default=0, verbose_name="Inovação e Criatividade (0-10)")

    comentario = models.TextField(blank=True, verbose_name="Comentários e Feedback")
    avaliado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['projeto', 'professor']

    def __str__(self):
        return f"Avaliação de {self.projeto.titulo} por {self.professor.get_full_name()}"

    @property
    def media(self):
        notas = [self.nota_desenvolvimento, self.nota_documentacao,
                 self.nota_apresentacao, self.nota_inovacao]
        return round(sum(notas) / len(notas), 1)

    @property
    def media_cor(self):
        if self.media >= 7:
            return 'success'
        elif self.media >= 5:
            return 'warning'
        return 'danger'
