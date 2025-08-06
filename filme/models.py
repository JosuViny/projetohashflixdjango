from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

LISTA_CATEGORIAS = (
    ('acao', 'Ação'),
    ('aventura', 'Aventura'),
    ('comedia', 'Comédia'),
    ('drama', 'Drama'),
    ('terror', 'Terror'),
    ('romance', 'Romance'),
    ('suspense', 'Suspense'),
    ('documentario', 'Documentário'),
)

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    vizualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


# criar os episódios
class Episodio(models.Model):
    filme = models.ForeignKey('Filme', related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return f'{self.filme.titulo} | {self.titulo}'

# criar o usuário
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')