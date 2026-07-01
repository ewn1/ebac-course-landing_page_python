# MODELO DE ENTIDADE

from django.db import models
from django.contrib.auth.models import User # modelo pré construido de usuários, permissões. (para não reinventar a roda :T)


STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='site_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

class Meta:
    ordering = ['-created_on'] # o sinal de - vai ordenar os posts criados de forma decrescente, o contrário coloca em ordem crescente.

def __str__(self):
    return self.title