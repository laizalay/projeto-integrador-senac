from django.core.management.base import BaseCommand
from core.models import Usuario, Projeto


class Command(BaseCommand):
    help = 'Cria usuários e dados de demonstração'

    def handle(self, *args, **kwargs):
        usuarios = [
            {
                'username': 'admin',
                'email': 'admin@senac.br',
                'first_name': 'Administrador',
                'last_name': 'Sistema',
                'papel': 'admin',
                'password': 'admin123',
                'is_superuser': True,
                'is_staff': True,
            },
            {
                'username': 'coordenador',
                'email': 'coord@senac.br',
                'first_name': 'Coordenador',
                'last_name': 'Senac',
                'papel': 'coordenador',
                'password': 'coord123',
                'turma': '',
            },
            {
                'username': 'professor',
                'email': 'professor@senac.br',
                'first_name': 'Professor',
                'last_name': 'Senac',
                'papel': 'professor',
                'password': 'prof123',
                'turma': '',
            },
            {
                'username': 'aluno1',
                'email': 'aluno1@senac.br',
                'first_name': 'Maria',
                'last_name': 'Silva',
                'papel': 'aluno',
                'password': 'aluno123',
                'turma': 'ADS-2026-M',
            },
            {
                'username': 'aluno2',
                'email': 'aluno2@senac.br',
                'first_name': 'João',
                'last_name': 'Santos',
                'papel': 'aluno',
                'password': 'aluno123',
                'turma': 'ADS-2026-N',
            },
        ]

        for dados in usuarios:
            if not Usuario.objects.filter(username=dados['username']).exists():
                u = Usuario(
                    username=dados['username'],
                    email=dados['email'],
                    first_name=dados['first_name'],
                    last_name=dados['last_name'],
                    papel=dados['papel'],
                    turma=dados.get('turma', ''),
                    is_superuser=dados.get('is_superuser', False),
                    is_staff=dados.get('is_staff', False),
                )
                u.set_password(dados['password'])
                u.save()
                self.stdout.write(self.style.SUCCESS(
                    f'✅ Criado: {dados["first_name"]} ({dados["papel"]}) — {dados["username"]} / {dados["password"]}'
                ))
            else:
                self.stdout.write(f'⏭  Já existe: {dados["username"]}')

        # Criar projetos de demonstração
        aluno1 = Usuario.objects.filter(username='aluno1').first()
        aluno2 = Usuario.objects.filter(username='aluno2').first()

        if aluno1 and not Projeto.objects.filter(autor=aluno1).exists():
            Projeto.objects.create(
                titulo='Sistema de Agendamento Online',
                descricao='Plataforma web para agendamento de serviços em salões de beleza, com autenticação, calendário interativo e notificações.',
                tecnologias='Python, Django, SQLite, HTML, CSS, JavaScript',
                link_github='https://github.com/exemplo/agendamento',
                status='concluido',
                turma='ADS-2026-M',
                autor=aluno1,
            )
            self.stdout.write(self.style.SUCCESS('✅ Projeto de demonstração criado (Maria)'))

        if aluno2 and not Projeto.objects.filter(autor=aluno2).exists():
            Projeto.objects.create(
                titulo='App de Controle Financeiro',
                descricao='Aplicativo para controle de receitas e despesas pessoais, com dashboard de gráficos e relatórios mensais.',
                tecnologias='Python, Flask, SQLite, Chart.js, Bootstrap',
                link_github='https://github.com/exemplo/financeiro',
                status='desenvolvimento',
                turma='ADS-2026-N',
                autor=aluno2,
            )
            self.stdout.write(self.style.SUCCESS('✅ Projeto de demonstração criado (João)'))

        self.stdout.write(self.style.SUCCESS('\n🚀 Dados de demonstração prontos!'))
