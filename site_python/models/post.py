# MODELO DE ENTIDADE

from django.db import models  # Importa as ferramentas de banco de dados do Django (tipos de campos, etc.).
from django.contrib.auth.models import User  # Modelo pré-construído de usuários (perfeito seu comentário, roda pronta!).


# O que é essa tupla STATUS?
# É um mapeamento de "Chave e Valor". No banco de dados, para economizar espaço e performance, 
# nós salvamos apenas os números (0 ou 1). Mas para o usuário ou no painel Admin, o Django 
# vai mostrar os textos amigáveis ('Draft' para rascunho, 'Publish' para publicado).
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):  # Define a classe Post, que herda de models.Model para o Django saber que isso é uma tabela.
    
    # Campo de texto curto para o título. Limite de 200 caracteres. 
    # 'unique=True' impede que existam dois posts com o mesmíssimo título.
    title = models.CharField(max_length=200, unique=True)
    
    # O 'slug' é a parte amigável da URL (ex: em vez de 'site.com/p?id=12', fica 'site.com/meu-primeiro-post').
    # Também é único para não confundir as páginas do site.
    slug = models.SlugField(max_length=200, unique=True)
    
    # RELACIONAMENTO: Chave Estrangeira (ForeignKey)
    # Vincula o Post a um Usuário da tabela 'User'. 
    # 'on_delete=models.CASCADE' significa: se o usuário for deletado, todos os posts dele somem juntos.
    # 'related_name' permite que, a partir de um usuário, você busque os posts dele fazendo: usuario.site_posts.all()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='site_posts')
    
    # Campo de data e hora. O 'auto_now=True' faz o Django atualizar esse campo AUTOMATICAMENTE 
    # com o horário atual toda vez que você editar e salvar o post.
    updated_on = models.DateTimeField(auto_now=True)
    
    # Campo de texto longo, sem limite de caracteres. É onde vai o corpo/conteúdo do artigo do blog.
    content = models.TextField()
    
    # Campo de data e hora. O 'auto_now_add=True' carimba a data/hora uma ÚNICA vez: 
    # o momento exato em que o post foi criado. Depois, ele nunca mais muda.
    created_on = models.DateTimeField(auto_now_add=True)
    
    # Campo de número inteiro. Usa a tupla STATUS lá de cima para limitar as opções (choices).
    # Se você não definir o status ao criar o post, ele começa como 0 (Draft/Rascunho).
    status = models.IntegerField(choices=STATUS, default=0)

    # Para o Django entender que eles pertencem ao Post, eles DEVEM ficar identados (para dentro) da classe Post!
    class Meta:
        # Define a ordenação padrão dos posts quando você puxar do banco.
        # O sinal de '-' significa ordem decrescente (do mais novo para o mais antigo).
        ordering = ['-created_on']

    # Método especial do Python. Sempre que o Django precisar mostrar o post como texto (tipo no painel Admin),
    # em vez de mostrar um código feio como "<Post object (1)>", ele vai mostrar o título real do post.
    def __str__(self):
        return self.title