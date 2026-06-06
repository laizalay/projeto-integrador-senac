from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario, Projeto


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'placeholder': 'seu@email.com', 'autofocus': True})
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
        fields = ['first_name', 'last_name', 'username', 'email', 'papel', 'password']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Nome de usuário',
            'email': 'E-mail',
            'papel': 'Papel',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'tecnologias', 'link_github', 'status']
        labels = {
            'titulo': 'Título do Projeto',
            'descricao': 'Descrição',
            'tecnologias': 'Tecnologias Utilizadas',
            'link_github': 'Link do GitHub',
            'status': 'Status',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ex: Sistema de Agendamento Online'}),
            'descricao': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Descreva o objetivo, problema resolvido e funcionalidades...'}),
            'tecnologias': forms.TextInput(attrs={'placeholder': 'Python, Django, SQLite, HTML, CSS'}),
            'link_github': forms.URLInput(attrs={'placeholder': 'https://github.com/usuario/repositorio'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
