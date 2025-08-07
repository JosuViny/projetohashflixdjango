from django.apps import AppConfig
from django.db import connection


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        from .models import Usuario
        import os

        # Verificar se a tabela existe antes de fazer query
        if 'filme_usuario' in connection.introspection.table_names():
            email = os.getenv('EMAIL_ADMIN')
            senha = os.getenv('SENHA_ADMIN')

            if email and senha:
                usuarios = Usuario.objects.filter(email=email)
                if not usuarios:
                    Usuario.objects.create_superuser(
                        username='admin', 
                        email=email, 
                        password=senha, 
                        is_active=True, 
                        is_staff=True
                    )