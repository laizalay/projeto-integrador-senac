from django.core.management.base import BaseCommand
from core.models import Usuario

class Command(BaseCommand):
    help = 'Cria o administrador padrão se não existir'

    def handle(self, *args, **kwargs):
        if not Usuario.objects.filter(email='admin@senac.br').exists():
            u = Usuario.objects.create_superuser(
                username='admin',
                email='admin@senac.br',
                password='admin123',
                first_name='Administrador',
                papel='admin'
            )
            self.stdout.write(self.style.SUCCESS('✅ Admin criado: admin@senac.br / admin123'))
        else:
            self.stdout.write('Admin já existe.')
