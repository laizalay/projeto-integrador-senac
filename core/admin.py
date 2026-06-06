from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Projeto


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'papel', 'is_active']
    list_filter = ['papel', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Nexus PI', {'fields': ('papel', 'bio')}),
    )


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'status', 'criado_em']
    list_filter = ['status']
    search_fields = ['titulo', 'descricao', 'autor__username']
