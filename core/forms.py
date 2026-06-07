from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario, Projeto, Avaliacao


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(attrs={'placeholder': 'seu usuário', 'autofocus': True})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Mínimo 6 caracteres'}),
        min_length=6
    )

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'papel', 'turma', 'password']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Nome de usuário',
            'email': 'E-mail',
            'papel': 'Papel',
            'turma': 'Turma',
        }

    def __init__(self, *args, **kwargs):
        self.usuario_logado = kwargs.pop('usuario_logado', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['turma'].required = False
        # Só admin pode cadastrar outro admin
        if not self.usuario_logado or self.usuario_logado.papel != 'admin':
            self.fields['papel'].choices = [
                (k, v) for k, v in self.fields['papel'].choices
                if k != 'admin'
            ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UsuarioEditarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'papel', 'turma']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Nome de usuário',
            'email': 'E-mail',
            'papel': 'Papel',
            'turma': 'Turma',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['turma'].required = False


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'tecnologias', 'link_github', 'turma', 'membros_grupo', 'status']
        # status 'avaliado' é definido automaticamente pelo professor
        labels = {
            'titulo': 'Título do Projeto',
            'descricao': 'Descrição',
            'tecnologias': 'Tecnologias Utilizadas',
            'link_github': 'Link do GitHub',
            'turma': 'Turma',
            'membros_grupo': 'Membros do Grupo',
            'status': 'Status',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ex: Sistema de Agendamento Online'}),
            'descricao': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Descreva o objetivo, problema resolvido e funcionalidades...'}),
            'tecnologias': forms.TextInput(attrs={'placeholder': 'Python, Django, SQLite, HTML, CSS'}),
            'link_github': forms.URLInput(attrs={'placeholder': 'https://github.com/usuario/repositorio'}),
            'turma': forms.TextInput(attrs={'placeholder': 'Ex: ADS-2025-1'}),
            'membros_grupo': forms.TextInput(attrs={'placeholder': 'Ex: João Silva, Maria Santos, Pedro Oliveira'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['turma'].required = False
        self.fields['membros_grupo'].required = False
        # Remove 'avaliado' — definido automaticamente pelo professor
        self.fields['status'].choices = [
            (k, v) for k, v in self.fields['status'].choices
            if k != 'avaliado'
        ]


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota_desenvolvimento', 'nota_documentacao',
                  'nota_apresentacao', 'nota_inovacao', 'comentario']
        labels = {
            'nota_desenvolvimento': 'Desenvolvimento Técnico',
            'nota_documentacao': 'Documentação',
            'nota_apresentacao': 'Apresentação',
            'nota_inovacao': 'Inovação e Criatividade',
            'comentario': 'Comentários e Feedback',
        }
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Deixe seu feedback sobre o projeto...'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
